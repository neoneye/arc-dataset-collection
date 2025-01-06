# ARC-Heavy

- [BARC Synthetic Examples](https://www.basis.ai/arc_interface/examples) - visualization and navigate the datasets and corresponding code for each puzzle.
- Repo: [github](https://github.com/xu3kev/BARC)
- Datasets: [huggingface](https://huggingface.co/collections/barc0/synthetic-arc-dataset-6725aa6031376d3bacc34f76)
- Authors: Wen-Ding Li, Keya Hu, Carter Larsen, Yuqing Wu, Simon Alford, Caleb Woo, Spencer M. Dunn, Hao Tang, Michelangelo Naim, Dat Nguyen, Wei-Long Zheng,
Zenna Tavares, Yewen Pu, Kevin Ellis
- License: MIT

### Directory `data`

The `"data"` dir contains a tiny subset of ARC-Heavy. I have cherry picked around 300 of the puzzles, since ARC-Interactive cannot render all thumbnails for all 400.000 puzzles.

- The `data/a` dir contains 300 cherrypicked puzzles from `data_100k`.

- The `data/b` dir contains 300 cherrypicked puzzles from `data_suggestfunction_100k`.

- The `data/c` dir contains 300 cherrypicked puzzles from `100k-gpt4-description-gpt4omini-code_generated_problems`.

- The `data/d` dir contains 300 cherrypicked puzzles from `100k_gpt4o-mini_generated_problems`.

- [ARC-Interactive - a](https://neoneye.github.io/arc/?dataset=ARC-Heavy-a)
- [ARC-Interactive - b](https://neoneye.github.io/arc/?dataset=ARC-Heavy-b)
- [ARC-Interactive - c](https://neoneye.github.io/arc/?dataset=ARC-Heavy-c)
- [ARC-Interactive - d](https://neoneye.github.io/arc/?dataset=ARC-Heavy-d)


### Directory `data_100k`

This comes from the `data_100k.jsonl` file in this [repo](https://huggingface.co/datasets/barc0/200k_HEAVY_gpt4o-description-gpt4omini-code_generated_problems/tree/main).

This is named `Heavy` on basis.ai.

### Directory `data_suggestfunction_100k`

This comes from the `data_suggestfunction_100k.jsonl` file in this [repo](https://huggingface.co/datasets/barc0/200k_HEAVY_gpt4o-description-gpt4omini-code_generated_problems/tree/main).

This is named `Heavy with suggestions` on basis.ai.

### Directory `100k-gpt4-description-gpt4omini-code_generated_problems`

This comes from the `100k-gpt4-description-gpt4omini-code_generated_problems.jsonl` file in this [repo](https://huggingface.co/datasets/barc0/100k-gpt4-description-gpt4omini-code_generated_problems).

This is named `GPT-4` on basis.ai.

### Directory `100k_gpt4o-mini_generated_problems`

This comes from the `100k_gpt4o-mini_generated_problems.jsonl` file in this [repo](https://huggingface.co/datasets/barc0/100k-gpt4omini-description-gpt4omini-code_generated_problems).

This is named `GPT4o-mini` on basis.ai.
