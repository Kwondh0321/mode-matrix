# mode-matrix

[한국어](README.md)

Summarize POSIX permission modes in a directory tree.

A small, dependency-free Python command-line tool that does one job well:
**summarize file modes**.

## Highlights

- Focused CLI with predictable text output
- Python standard library only at runtime
- Importable core functions for reuse in scripts
- Unit tests and GitHub Actions CI

## Requirements

Python 3.11 or newer.

## Install

~~~bash
git clone https://github.com/Kwondh0321/mode-matrix.git
cd mode-matrix
python -m pip install .
~~~

For an isolated command-line installation, pipx install . also works.

## Quick start

~~~bash
mode-matrix .
~~~

Run mode-matrix --help for every option.

## Development

~~~bash
python -m unittest discover -s tests -v
python mode_matrix.py --help
~~~

## Scope

This repository intentionally stays small. It favors transparent behavior,
standard formats, and composability with shell pipelines over a large
dependency tree or an interactive interface.

## License

MIT
