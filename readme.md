# Multiple datasets for ARC (Abstraction and Reasoning Corpus)

Each dataset have its own license, see the readme/license for details.

The datasets can be inspected here: [ARC-Interactive](https://neoneye.github.io/arc/)

# Question & Answer

### What are `_v2.json` files?

Ideally there should be no suffixes. The `_v2` and `_v3` suffixes are my kludgy workaround. However when recording interaction histories, then one interaction history file references a specific version of a task. When a task gets fixed upstream, then the old solution may no longer be the correct solution for the new task. And deleting old interaction history files that would be sad. So `_v` it was.

If there is a `_v` suffix then the newest is the highest version.

I also considered going with commit ids, but that would have made it even more tricky to keep track of.

