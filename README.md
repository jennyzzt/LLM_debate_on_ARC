# Foundation Model Debate on ARC Dataset

The [LLM-Debate paper](https://arxiv.org/abs/2305.14325) showed that having LLMs engage in debate can significantly enhance their mathematical and strategic reasoning skills. Can this debate approach improve LLMs performance on the [ARC dataset](https://arcprize.org/)?

<p align="center">
  <img src="https://github.com/jennyzzt/LLM_debate_on_ARC/assets/53294998/d626a591-f2cb-4203-9d9a-d7e3aa7962b6" width="300">
  <img src="https://github.com/jennyzzt/LLM_debate_on_ARC/assets/53294998/90d292db-241a-4498-9cec-98be94c1f37b" width="300">
  <br>
  <em>Examples of ARC dataset, taken from <a href="https://twitter.com/fchollet/status/1800577423853195451">this X thread</a>.</em>
</p>

## Contents

- [Results Summary](#results-summary)
  - Different number of Agents
  - Different rounds of Debate
- [Repo Walkthrough](#repo-walkthrough)
  - [Download ARC Dataset](#download-arc-dataset)
  - [Setup](#setup)
  - [Run Debate](#run-debate)
  - [Make Plots](#make-plots)
- [Possible Extensions](#possible-extensions)

## Results Summary

<details>
<summary>Click to expand</summary>

This study explores two approaches for eliciting outputs from Large Language Models (LLMs) in tasks that can be represented through input and output matrices: (1) **Direct**, where the LLM is requested to directly produce the solution matrix, and (2) **Code**, where the LLM is tasked with generating the code that, when executed, will generate the solution matrix. In a given task, the pattern extracted from the demonstrations is consistent with that required for the test case. Hence, code generation provides more interpretable evidence of the LLM's comprehension of the underlying patterns.

Given the difficulty of tasks in the ARC dataset, this study adopts a nuanced approach for evaluating responses. Rather than categorizing answers strictly as correct or incorrect, we assess them based on the percentage of elements (numbers) in the response (the output matrix) that align with the correct solution. This method allows for a more granular understanding of performance, potentially providing better insights into the effectiveness of the debate mechanism in enhancing reasoning capabilities.

We evaluate on two LLM settings: (1) **GPT-4**, a stronger but closed sourced model by OpenAI, and (2) **Gemma**, an open-source model by Google Deepmind accessible through Hugging Face. Since Gemma does not have a system prompt component and has a shorter context window, system prompts are provided to GPT-4 only. The same user prompts are used for both GPT-4 and Gemma (Appendix A). For computation efficiency, we only evaluate on 10 data points from the ARC dataset.

**Number of Agents.** First, we analyze how the number of agents affect the performance. We increase the number of agents used in the debate (from one to three), while fixing the number of debate rounds to be two. There is no clear trend that increasing the number of debate rounds will definitely lead to higher performance. Having more agents only increased the performance in the Direct-Gemma setting.

![diffagents](https://github.com/jennyzzt/LLM_debate_on_ARC/assets/53294998/fa1e035d-552d-4ace-8796-23df428484c2)
Average score achieved against the number of agents participating in the debate, with the number of debate rounds fixed to two.

**Rounds of Debate.** Next, we analyze how the number of debate rounds affect the performance. We increase the number of debate rounds (from one to three), while fixing the number of agents to be two. There is no clear trend that increasing the number of debate rounds will definitely lead to higher performance. Having more debate rounds only increased the performance in the Code-Gemma setting. In the Code-GPT-4 and Direct-Gemma settings, having more debate rounds actually decreased performance.

![diffrounds](https://github.com/jennyzzt/LLM_debate_on_ARC/assets/53294998/9711d2fa-c702-4757-af2c-ffaa6e7b2f63)
Average score achieved against the number of debate rounds, with the number of agents fixed to two.
</details>

## Repo Walkthrough

<details>
<summary>Click to expand</summary>

### Download ARC dataset
- Download and unzip https://lab42.global/wp-content/uploads/2022/08/ARC-800-tasks.zip
- Rename dataset `mv ARC-800-tasks/ ARC_dataset/`
- Generate ARC task images `python create_arc_images.py`
    - Images are stored in `ARC_dataset/training_images` and `ARC_dataset/evaluation_images`

### Setup
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install accelerate
```

### Run debate
```
python gen_arc.py  --agents N --rounds N --n-data N --direct --soft-eval --model gemma
```
- `--agents` how many agents debating with each other
- `--rounds` how many rounds the agents will debate with each other
- `--n-data` number of datapoints to evaluate on (default: -1 is all)
- `--direct` ask the FM to directly output the solution instead of writing code
- `--soft-eval` the score is not just 0 or 1, but the percentage of how many numbers match
- `--model [openai, gemma]` which FM to use

bash script to run all experiments
```
bash ./run_gemma.sh
bash ./run_openai.sh
```

### Make plots
```
python plot_arc.py --agents N --rounds N
```
- make plots with fixed number of agents N
- make plots with fixed number of rounds N
</details>

## Possible extensions
- [ ] Using vision-language models instead of LLMs
- [ ] Evaluate more data samples
- [ ] Increasing the number of agents and debate rounds
