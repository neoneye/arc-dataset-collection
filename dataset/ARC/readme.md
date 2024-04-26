# The original ARC dataset

- Repo: [fchollet/ARC](https://github.com/fchollet/ARC/tree/master/data)
- Authors: François Chollet
- License: Apache-2.0 license

## Modifications

In response to open issues in the original ARC GitHub repository, I have provided fixes which are available in this repository. These fixed files are named with a `_v2.json` suffix, while the original files remain unchanged.

### List of fixes

Below are the issues from the original repository along with the corresponding fixes applied in this repository:

- **423a55dc**
  - **Issue**: [Test is unsolvable, skew](https://github.com/fchollet/ARC/issues/98)
  - **Fix**: `423a55dc_v2.json`

- **58e15b12**
  - **Issue**: [Test is unsolvable, missing magenta cell when green and aqua lines intersect](https://github.com/fchollet/ARC/issues/86)
  - **Fix**: `58e15b12_v2.json`

- **a8610ef7**
  - **Issue**: [Test is unsolvable, all cyan cells should be grey](https://github.com/fchollet/ARC/issues/89)
  - **Fix**: `a8610ef7_v2.json`

- **b4a43f3b**
  - **Issue**: [Test is unsolvable, missing 2 green pixels](https://github.com/fchollet/ARC/issues/101)
  - **Fix**: `b4a43f3c_v2.json` (Note: Verify file name, as it differs from the issue code)

- **bd14c3bf**
  - **Issue**: [Minor inconsistency, top left object should be red](https://github.com/fchollet/ARC/issues/73)
  - **Fix**: `bd14c3bf_v2.json`

- **dc433765**
  - **Issue**: [Minor inconsistency, redundant train and test](https://github.com/fchollet/ARC/issues/29)
  - **Fix**: `dc433765_v2.json`
