# ARC-Heavy

- [BARC Synthetic Examples](https://www.basis.ai/arc_interface/examples) - visualization and navigate the datasets and corresponding code for each puzzle.
- Repo: [github](https://github.com/xu3kev/BARC)
- Datasets: [huggingface](https://huggingface.co/collections/barc0/synthetic-arc-dataset-6725aa6031376d3bacc34f76)
- Authors: Wen-Ding Li, Keya Hu, Carter Larsen, Yuqing Wu, Simon Alford, Caleb Woo, Spencer M. Dunn, Hao Tang, Michelangelo Naim, Dat Nguyen, Wei-Long Zheng,
Zenna Tavares, Yewen Pu, Kevin Ellis
- License: MIT

The `"data"` dir contains a tiny subset of ARC-Heavy. I have cherry picked around 300 of the puzzles, since ARC-Interactive cannot render all thumbnails for all 400.000 puzzles.

### `data_100k`

This comes from the `data_100k.jsonl` file in this [repo](https://huggingface.co/datasets/barc0/200k_HEAVY_gpt4o-description-gpt4omini-code_generated_problems/tree/main).

The `data/a` dir contains 300 cherrypicked puzzles from the `data_100k`. This is named `Heavy` on basis.ai.

- [ARC-Interactive - a](https://neoneye.github.io/arc/?dataset=ARC-Heavy-a)

### `data_suggestfunction_100k`

This comes from the `data_suggestfunction_100k.jsonl` file in this [repo](https://huggingface.co/datasets/barc0/200k_HEAVY_gpt4o-description-gpt4omini-code_generated_problems/tree/main).

The `data/b` dir contains 300 cherrypicked puzzles from the `data_suggestfunction_100k`. This is named `Heavy with suggestions` on basis.ai.

- [ARC-Interactive - b](https://neoneye.github.io/arc/?dataset=ARC-Heavy-b)
