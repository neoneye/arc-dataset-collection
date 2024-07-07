# synth_riddles

This is a tiny extract of the dataset. I have cherry picked a few files from each compressed file, avoiding tasks that are too hard or broken or redundant.
The compressed files are included in this repo, so you can unzip if needed.

The file: `e_009d5c81_10x10_250k.tar.gz` contains 250.000 files. It's one single type of task.
I have encountered a few of the tasks that are invalid.

The file: `rigid_15x15_depth_1_10k.tar.gz` contains 10.000 files. Flip and rotate operations.

The files: `rigid_and_half_depth_1_10k.tar.gz`, `rigid_and_half_depth_2_10k.tar.gz` each contain 10.000 files. Crop in half operations.

The files: `all_depth_2_10k.tar.gz`, `all_depth_3_10k.tar.gz`, `all_depth_5_10k.tar.gz`, `unary_depth_2_10k.tar.gz` each contain 10.000 files.
IMO The majority of tasks are garbage. Too complex for me to verify if they make sense or not. Most of them seems to make no sense.
In ARC the biggest canvas is `30x30`. However here some of the tasks have a canvas size that is bigger than `30x30`, such as `eee6d929.json` and `ed7a3761.json` where the output size is `31x1`.
I found a few good tasks, so I have added those to this repo.

- [ARC-Interactive](https://neoneye.github.io/arc/?dataset=synth_riddles)
- Repo: [synth_riddles](https://github.com/arc-community/synth_riddles)
- Authors: Andreas Köpf
- License: MIT
