# Convert json files

The json files inside the [IPARC_ChallengeV2](https://github.com/ac20/IPARC_ChallengeV2/tree/main/Dataset) repository has a slightly different format than the typical ARC files.

This script takes the the `IPARC_ChallengeV2/Dataset` dir as dir named `input`.

Then run `python a.py`. It flattens the nested directory structure.

Then run `python b.py`. It takes the last input/output pair and turns it into a test pair.

Now the `output_b` dir contains the converted dataset.
