import argparse
import copy
import concurrent.futures
import numpy as np
import time
import re
import os
import json
import importlib.util
import sys
from openai import OpenAI
from transformers import AutoTokenizer, pipeline
import torch


def file_to_string(filepath):
    with open(filepath, 'r') as f:
        data = f.read().strip()
    return data

def format_arc_data(arc_data, direct=False):
    # Get task demo string
    task_demo_str = ''
    for demo in arc_data['train']:
        task_demo_str += '```\n'
        task_demo_str += f'input = {demo["input"]}\n'
        task_demo_str += f'output = {demo["output"]}\n'
        task_demo_str += '```\n'

    # Get task test string
    task_test_str = ''
    for testcase in arc_data['test']:
        task_test_str += '```\n'
        task_test_str += f'input = {testcase["input"]}\n'
        task_test_str += '```\n'
        if direct:  # Only take one test case
            break

    return task_demo_str, task_test_str

def load_fn_from_filepath(filepath, function_name):
    # Load a function from a given filepath
    try:
        module_name = 'gen_arc'
        spec = importlib.util.spec_from_file_location(module_name, filepath)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        sys.modules[module_name] = module
        function = getattr(module, function_name)
    except:  # if function is not loadable
        function = lambda x : x
    return function

def load_solution_from_filepath(filepath, var_name):
    # Load a variable from a given filepath
    try:
        module_name = 'gen_arc'
        spec = importlib.util.spec_from_file_location(module_name, filepath)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        sys.modules[module_name] = module
        solution = getattr(module, var_name)
    except:  # if solution is not loadable
        solution = []
    return solution

def get_percentage_match(arr1, arr2):
    score = 0
    for i, xs in enumerate(arr1):
        for j, x in enumerate(xs):
            try:
                if len(arr2) > i and len(arr2[i]) > j and arr2[i][j] == x:
                    score += 1
            except:
                pass
    score = score / (len(arr1) * len(arr1[0]))
    return score

def eval_algo(solve_fn, arc_data, soft_eval=False):
    # Calculate percentage of test cases done correctly
    testcases = arc_data['test']
    scores = []
    for testcase in testcases:
        input = testcase['input']
        output = testcase['output']
        gen_output = None
        # Run solve_fn with timeout
        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
            try:
                future = executor.submit(solve_fn, input)
                try:
                    gen_output = future.result(timeout=30)
                except concurrent.futures.TimeoutError:
                    future.cancel()
            except:  # if the function does not work
                continue
        # Check if correct output
        if soft_eval:
            score = get_percentage_match(output, gen_output)
        else:
            score = 1 if output == gen_output else 0
        scores.append(score)
    return np.mean(scores)

def eval_solution(solution, arc_data, soft_eval=False):
    output = arc_data['test'][0]['output']
    if soft_eval:
        score = get_percentage_match(output, solution)
    else:
        score = 1 if output == solution else 0
    return score

def construct_debate_message(agent_contexts_other, idx, direct=False):
    if len(agent_contexts_other) == 0:
        # Self-reflect when there are no other agents
        content = file_to_string(f'./prompts/reflect_user{get_promptfile_suffix(direct)}.txt')
    else:
        # Include other agent responses in prompt
        content = file_to_string(f'./prompts/debate_user{get_promptfile_suffix(direct)}.txt')
        other_agent_opinions = ''
        for agent_context in agent_contexts_other:
            agent_response = agent_context[idx]['content']
            response = "\n\nOne agent's response: ```{}```".format(agent_response)
            other_agent_opinions += response
        content = content.replace('{{ OTHER_AGENT_OPINIONS }}', other_agent_opinions)

    return {"role": "user", "content": content}

def generate_completion_openai(agent_context, client):
    try:
        completion = client.chat.completions.create(
            # model="gpt-3.5-turbo",
            model="gpt-4-0125-preview",
            messages=agent_context,
            temperature=0.2,
            max_tokens=4096,
        )
    except Exception as e:
        print(f"Retrying due to an error: {e}")
        time.sleep(20)
        return generate_completion_openai(agent_context, client)
    return completion.choices[0].message.content

def generate_completion_gemma(agent_context, pipeline):
    # Pass into gemma pipeline
    prompt = pipeline.tokenizer.apply_chat_template(
        agent_context[1:],  # Reformat context to exclude system role
        tokenize=False,
        add_generation_prompt=True
    )
    completion = pipeline(
        prompt,
        max_new_tokens=512,
        do_sample=True,
        temperature=0.2,
    )
    return completion[0]["generated_text"][len(prompt):]

def save_generated_algo(agent_folder, response_message, round):
    proper_code = False
    try:
        code_string = re.search(r'```python(.*?)```', response_message, re.DOTALL)
        code_string = code_string.group(1).strip()
        proper_code = True
    except:
        # if output does not contain python code block, return identify fn
        print('No python code block, using identify function:')
        print(response_message)
        code_string = file_to_string('./prompts/identify_fn.py')
    # save with round number
    with open(os.path.join(agent_folder, f'./algo{round}.py'), 'w') as f:
        f.write(code_string)
    # save as final algo
    if proper_code or round == 0:
        with open(os.path.join(agent_folder, f'./algo.py'), 'w') as f:
            f.write(code_string)

def save_generated_solution(agent_folder, response_message, round):
    proper_solution = False
    try:
        solution_string = re.findall(r'```(.*?)```', response_message, re.DOTALL)
        solution_string = solution_string[-1].strip()
        if 'output' not in solution_string:
            solution_string = 'output = ' + solution_string
        proper_solution = True
    except:
        # if output does not contain solution block, return identify fn
        print('No solution block, using dummy solution:')
        print(response_message)
        solution_string = 'output = []'
    # save with round number
    with open(os.path.join(agent_folder, f'./solution{round}.py'), 'w') as f:
        f.write(solution_string)
    # save as final algo
    if proper_solution or round == 0:
        with open(os.path.join(agent_folder, f'./solution.py'), 'w') as f:
            f.write(solution_string)

def get_promptfile_suffix(direct):
    return '_direct' if direct else ''


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--agents", type=int, default=2, help="number of agents (default: 2)")
    parser.add_argument("--rounds", type=int, default=2, help="number of debate rounds (default: 2)")
    parser.add_argument("--n-data", type=int, default=-1, help="number of datapoints to use, -1 means all (default: -1)")
    parser.add_argument("--direct", action="store_true", default=False, help="ask FM to directly output the solution (default: False)")
    parser.add_argument("--soft-eval", action="store_true", default=False, help="eval the solutions by percentage instead of binary (default: False)")
    parser.add_argument("--model", type=str, default="openai", help="model to use (default: openai's gpt-4-0125-preview)")
    args = parser.parse_args()

    # Parameters
    agents = args.agents
    rounds = args.rounds
    n_data = args.n_data

    # Read ARC dataset
    arc_dir = './ARC_dataset/training/'
    arc_files = []
    for filename in os.listdir(arc_dir):
        if os.path.isfile(os.path.join(arc_dir, filename)):
            arc_files.append(filename)
            if n_data > 0 and len(arc_files) >= n_data:
                break

    if args.model == "openai":
        # Create OpenAI client
        client = OpenAI()
    elif args.model == "gemma":
        # Create gemma pipeline
        model = "google/gemma-2b-it"
        tokenizer = AutoTokenizer.from_pretrained(model)
        pipeline = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            model_kwargs={
                "torch_dtype": torch.bfloat16,
                "quantization_config": {"load_in_4bit": True},
            },
        )

    # Evaluate on dataset
    all_generated_data = {}
    run_folder = f'./ARC_gen_agents{agents}_rounds{rounds}_{args.model}{get_promptfile_suffix(args.direct)}'
    for arc_file in arc_files:
        # Get ARC question
        arc_id = arc_file.split('.')[0]
        print(f'Debating about problem {arc_file}')
        with open(os.path.join(arc_dir, arc_file), 'r') as file:
            arc_data = json.load(file)

        # Folder to save outputs
        save_folder = os.path.join(run_folder, arc_id)
        os.makedirs(save_folder, exist_ok=True)
        for i in range(agents):
            agent_folder = os.path.join(save_folder, f'./agent{i}')
            os.makedirs(agent_folder, exist_ok=True)

            # Format prompts
            system_prompt = file_to_string(f'./prompts/base_system{get_promptfile_suffix(args.direct)}.txt')
            user_prompt = file_to_string(f'./prompts/base_user{get_promptfile_suffix(args.direct)}.txt')
            task_demo_str, task_test_str = format_arc_data(arc_data, direct=args.direct)
            user_prompt = user_prompt.replace('{{ TASK_DEMOS }}', task_demo_str)
            user_prompt = user_prompt.replace('{{ TASK_TEST }}', task_test_str)

            # Generations
            generated_data = {}
            base_message = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ]
            agent_contexts = [copy.deepcopy(base_message) for _ in range(agents)]
            for round in range(rounds):
                for i, agent_context in enumerate(agent_contexts):
                    # Update context to debate
                    if round != 0:
                        agent_contexts_other = agent_contexts[:i] + agent_contexts[i+1:]
                        message = construct_debate_message(agent_contexts_other, 2*round, direct=args.direct)
                        agent_context.append(message)

                    # Generate completion
                    if args.model == 'openai':
                        response_message = generate_completion_openai(agent_context, client)
                    elif args.model == 'gemma':
                        response_message = generate_completion_gemma(agent_context, pipeline)
                    else:
                        raise ValueError(f"Model {args.model} not supported")

                    # Save assistant message
                    assistant_message = {"role": "assistant", "content": response_message}
                    agent_context.append(assistant_message)

                    if args.direct:
                        # Save generated solution
                        save_generated_solution(agent_folder, response_message, round)
                    else:
                        # Save generated algo
                        save_generated_algo(agent_folder, response_message, round)

        # Evaluate generated solutions
        agents_score = 0
        for agent in range(agents):
            if args.direct:
                solution = load_solution_from_filepath(os.path.join(save_folder, f'./agent{agent}/solution.py'), 'output')
                score = eval_solution(solution, arc_data, soft_eval=args.soft_eval)
            else:
                solve_fn = load_fn_from_filepath(os.path.join(save_folder, f'./agent{agent}/algo.py'), 'solve')
                score = eval_algo(solve_fn, arc_data, soft_eval=args.soft_eval)
            agents_score += score
        generated_data['score'] = agents_score / agents
        print('Avg score:', generated_data['score'])
        generated_data['gen'] = agent_contexts
        all_generated_data[arc_id] = generated_data

    # Save generated data
    with open(os.path.join(run_folder, 'generated_data.json'), "w") as f:
        json.dump(all_generated_data, f, indent=4)
