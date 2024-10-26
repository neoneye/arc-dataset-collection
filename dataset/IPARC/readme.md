# IPARC

- [ARC-Interactive](https://neoneye.github.io/arc/?dataset=IPARC)
- Dataset repo: [IPARC_ChallengeV2/Dataset](https://github.com/ac20/IPARC_ChallengeV2/tree/main/Dataset)
- Generator repo: [IPARC_ML](https://github.com/AniketTendulkar2510/IPARC_ML)
- Authors: Aditya Challa, Ashwin Srinivasan1, Michael Bain, and Gautam Shroff
- License: MIT

## Maybe avoid it

The `IPARC` dataset is hard. Out of the 600 tasks, only 5 have been solved by humans as of 2024-july-07, but most did a `Reveal` so they are disqualified. The other ARC like datasets have human solutions for almost all tasks. Thus `IPARC` doesn't reflect the kind of problems that humans can solve.

IMO A good dataset is something that can be solved by humans. Since `IPARC` cannot be solved by humans. Maybe avoid it.

## Invalid tasks

- [`CatB_Hard_Task005`](https://neoneye.github.io/arc/edit.html?dataset=IPARC&task=CatB_Hard_Task005) - images are blue/black, but red appear in the test output without any prior example.
- [`CatB_Hard_Task017`](https://neoneye.github.io/arc/edit.html?dataset=IPARC&task=CatB_Hard_Task017) - images are blue/black, but red appear in the test output without any prior example.
- [`CatB_Hard_Task019`](https://neoneye.github.io/arc/edit.html?dataset=IPARC&task=CatB_Hard_Task019) - images are blue/black, but red appear in the test output without any prior example.
- [`CatB_Hard_Task089`](https://neoneye.github.io/arc/edit.html?dataset=IPARC&task=CatB_Hard_Task089) - images are blue/black, but red appear in the test output without any prior example.

