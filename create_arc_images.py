import json
import os
import numpy as np
import matplotlib
from matplotlib import pyplot as plt


def add_grid(ax, array, label):
    ax.set_aspect('equal')
    cax = ax.pcolor(array, cmap=cmap, edgecolors='white')
    ax.axis('off')
    ax.title.set_text(label)

def add_qn_grid(ax, label):
    plt.text(0.5, 0.5, '?', transform=ax.transAxes, fontsize=50)
    ax.axis('off')
    ax.title.set_text(label)

def add_arrow(fig, ax1, ax2):
    arrow = matplotlib.patches.ConnectionPatch(
        [1, 0.5],
        [0, 0.5],
        coordsA='axes fraction',
        axesA=ax1, axesB=ax2,
        color="black",
        arrowstyle="->",
        mutation_scale=30,  # controls arrow head size
        linewidth=1,
    )
    fig.patches.append(arrow)


if __name__ == "__main__":
    split_names = ['training', 'evaluation']
    for split_name in split_names:
        # Read ARC dataset
        arc_dir = f'./ARC_dataset/{split_name}/'
        arc_files = []
        for filename in os.listdir(arc_dir):
            if os.path.isfile(os.path.join(arc_dir, filename)):
                arc_files.append(filename)
        save_folder = os.path.join(arc_dir, f'../{split_name}_images/')
        os.makedirs(save_folder, exist_ok=True)

        # Create colormap
        cmap = matplotlib.colors.ListedColormap([
            "black", "tab:blue", "tab:red", "tab:green", "yellow",
            "tab:gray", "tab:pink", "tab:orange", "tab:cyan", "tab:brown",
        ])

        for arc_file in arc_files:
            # Get ARC question
            arc_id = arc_file.split('.')[0]
            with open(os.path.join(arc_dir, arc_file), 'r') as file:
                arc_data = json.load(file)

            # Create image of task
            num_rows = len(arc_data['train']) + len(arc_data['test'])
            width = np.mean([len(xs['input']) for xs in arc_data['train']]) \
                + np.mean([len(xs['output']) for xs in arc_data['train']])
            height = np.sum([len(xs['input'][0]) for xs in arc_data['train']]) \
                + np.sum([len(xs['input'][0]) for xs in arc_data['test']])
            fig, axes = plt.subplots(num_rows, 2, figsize=(width/2, height/2))

            # Add train demos
            train_entries = arc_data['train']
            for i, train_entry in enumerate(train_entries):
                add_grid(axes[i, 0], np.array(train_entry['input']), f'Demo Input {i+1}')
                add_grid(axes[i, 1], np.array(train_entry['output']), f'Demo Output {i+1}')
                add_arrow(fig, axes[i, 0], axes[i, 1])

            # Add test cases
            test_entries = arc_data['test']
            for i, test_entry in enumerate(test_entries):
                add_grid(axes[len(arc_data['train']) + i, 0], np.array(test_entry['input']), f'Test Input {i+1}')
                # add_grid(axes[len(arc_data['train']) + i, 1], np.array(test_entry['output']), f'Test Output {i+1}')
                add_qn_grid(axes[len(arc_data['train']) + i, 1], f'Test Output {i+1}')
                add_arrow(fig, axes[len(arc_data['train']) + i, 0], axes[len(arc_data['train']) + i, 1])

            # Save image
            fig.tight_layout()
            fig.savefig(os.path.join(save_folder, f'./{arc_id}.png'), pad_inches=0)
            plt.close(fig)
