"""Summarize POSIX permission modes in a directory tree."""

import argparse
import stat
from collections import Counter
from pathlib import Path

def modes(root):
    result = Counter()
    for path in Path(root).rglob("*"):
        try:
            mode = stat.filemode(path.lstat().st_mode)
        except OSError:
            continue
        result[mode] += 1
    return result

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args(argv)
    for mode, count in sorted(modes(args.root).items()):
        print(f"{mode}\t{count}")

if __name__ == "__main__":
    main()
