# Foundation Model Debate

## Download ARC dataset
- Download and unzip https://lab42.global/wp-content/uploads/2022/08/ARC-800-tasks.zip
- Rename dataset `mv ARC-800-tasks/ ARC_dataset/`
- Generate ARC task images `python create_arc_images.py`
    - Images are stored in `ARC_dataset/training_images` and `ARC_dataset/evaluation_images`

## Setup
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install accelerate
```

## Run debate
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

## Make plots
```
python plot_arc.py --agents N --rounds N
```
- make plots with fixed number of agents N
- make plots with fixed number of rounds N
