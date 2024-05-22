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
  - **Fix 2**: `58e15b12_v2.json`
  - **Fix 3**: `58e15b12_v3.json`, commit `84e7398ea44fe906ed1b704814f746b3c6388c17` has a tailing newline. Otherise the same as v2.

- **a8610ef7**
  - **Issue 2**: [Test is unsolvable, all cyan cells should be grey](https://github.com/fchollet/ARC/issues/89)
  - **Fix 2**: `a8610ef7_v2.json`
  - **Issue 3**: [Minor inconsistency. 2 grey cells should be red](https://github.com/fchollet/ARC/commit/b7fd42c53f0c26a807ba0b00e42f858d2c11d125#diff-c9615dc3b4f3586bf08d44c1895878a70fa69e5e86a3b6d6b510fee6fe544b81)
  - **Fix 3**: `a8610ef7_v3.json`

- **b4a43f3b**
  - **Issue**: [Test is unsolvable, missing 2 green pixels](https://github.com/fchollet/ARC/issues/101)
  - **Fix**: `b4a43f3c_v2.json`

- **310f3251**
  - **Issue**: [Test is unsolvable, wrap around](https://github.com/fchollet/ARC/issues/99)
  - **Fix**: `310f3251_v2.json`

- **c92b942c**
  - **Issue**: [Minor inconsistency, remove wrap around in training pair 2](https://github.com/fchollet/ARC/commit/b7fd42c53f0c26a807ba0b00e42f858d2c11d125#diff-5449fd633a009a5f87bd1b7c19afd8048470161cc66bfced69ad0ffe8f2487a2)
  - **Fix**: `c92b942c_v2.json`

- **7039b2d7**
  - **Issue**: [Minor inconsistency, wrong number of columns](https://github.com/fchollet/ARC/pull/75)
  - **Fix**: `7039b2d7_v2.json`

- **bd14c3bf**
  - **Issue**: [Minor inconsistency, top left object should be red](https://github.com/fchollet/ARC/issues/73)
  - **Fix**: `bd14c3bf_v2.json`

- **dc433765**
  - **Issue**: [Minor inconsistency, redundant train and test](https://github.com/fchollet/ARC/issues/29)
  - **Fix**: `dc433765_v2.json`

- **e7b06bea**
  - **Issue**: [Minor inconsistency, missing grey cells](https://github.com/fchollet/ARC/pull/85)
  - **Fix**: `e7b06bea_v2.json`

- **469497ad**
  - **Issue**: [Minor inconsistency, Three pink blocks on the right should be orange](https://github.com/fchollet/ARC/pull/79)
  - **Fix**: `469497ad_v2.json`

- **6d0160f0**
  - **Issue**: [Minor inconsistency, Frame color shouldn't interfer with boxes](https://github.com/fchollet/ARC/pull/72)
  - **Fix**: `6d0160f0_v2.json`

- **54db823b**
  - **Issue**: [Minor inconsistency, Swap 2 pixels in first training pair](https://github.com/fchollet/ARC/commit/b7fd42c53f0c26a807ba0b00e42f858d2c11d125#diff-f0f2417d9757edfc08cee5fd123f4fac5a6b6941b20e348db88ca20e4118bd45)
  - **Fix**: `54db823b_v2.json`

- **b0f4d537**
  - **Issue**: [Minor inconsistency, middle line need move 1px righter](https://github.com/fchollet/ARC/issues/63)
  - **Fix**: `b0f4d537_v2.json`
