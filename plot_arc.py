import argparse
import numpy as np
import json
import re
import os
import matplotlib.pyplot as plt


def get_avg_score(gen_dir):
    # Get the average score from the results dir
    scores = []
    datapath = os.path.join(gen_dir, 'generated_data.json')
    if not os.path.exists(datapath):
        return None
    with open(datapath, 'r') as f:
        data = json.load(f)
        for _, entry_data in data.items():
            scores.append(entry_data['score'])
    return sum(scores) / len(scores)

def get_agent_count(gen_dir):
    # Get the number of agents from the results dir
    return int(gen_dir.split('_')[2].split('agents')[-1])

def get_round_count(gen_dir):
    # Get the number of rounds from the results dir
    return int(gen_dir.split('_')[3].split('rounds')[-1])

def get_promptfile_suffix(direct):
    return '_direct' if direct else ''


if '__main__' == __name__:
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--agents", type=int, default=2, help="number of agents (default: 2)")
    parser.add_argument("--rounds", type=int, default=2, help="number of debate rounds (default: 2)")
    parser.add_argument("--direct", action="store_true", default=False, help="ask FM to directly output the solution (default: False)")
    parser.add_argument("--model", type=str, default="openai", help="model to use (default: openai)")
    args = parser.parse_args()

    # Find all directories with generated data
    gen_dirs = []
    pattern = re.compile(f'ARC_gen_(.*)_{args.model}{get_promptfile_suffix(args.direct)}$')
    for folder in os.listdir('./'):
        if pattern.match(folder):
            gen_dirs.append(folder)

    # Get average scores
    avg_scores = {}
    for gen_dir in gen_dirs:
        avg_score = get_avg_score(gen_dir)
        if avg_score is not None:
            avg_scores[gen_dir] = get_avg_score(gen_dir)

    # Plot the scores against the number of rounds, fixed agents
    xs = []
    ys = []
    agents = args.agents
    for gen_dir, avg_score in avg_scores.items():
        if get_agent_count(gen_dir) != agents:
            continue
        rounds = get_round_count(gen_dir)
        xs.append(rounds)
        ys.append(avg_score)
    sorted_indices = np.argsort(xs)
    xs = np.array(xs)[sorted_indices]
    ys = np.array(ys)[sorted_indices]
    plt.plot(xs, ys, marker='o', linestyle='-')
    plt.xlabel('Number of rounds')
    plt.ylabel('Average score')
    plt.title(f'ARC task (number of agents = {agents})')
    plt.grid()
    plt.savefig(f'./arc_diffrounds_agents{agents}_{args.model}{get_promptfile_suffix(args.direct)}.png')
    plt.clf()

    # Plot the scores against the number of agents, fixed rounds
    xs = []
    ys = []
    rounds = args.rounds
    for gen_dir, avg_score in avg_scores.items():
        if get_round_count(gen_dir) != rounds:
            continue
        agents = get_agent_count(gen_dir)
        xs.append(agents)
        ys.append(avg_score)
    sorted_indices = np.argsort(xs)
    xs = np.array(xs)[sorted_indices]
    ys = np.array(ys)[sorted_indices]
    plt.plot(xs, ys, marker='o', linestyle='-')
    plt.xlabel('Number of agents')
    plt.ylabel('Average score')
    plt.title(f'ARC task (number of rounds = {rounds})')
    plt.grid()
    plt.savefig(f'./arc_diffagents_rounds{rounds}_{args.model}{get_promptfile_suffix(args.direct)}.png')
    plt.clf()
