# Simple template for a new Python project

## Requirements
- 3.7 <= Python < 3.11
- [poetry](https://python-poetry.org/docs/)
- git

## Packages will be installed:
- pytest 
- pytest-cov 
- tox 
- mkdocs-material 
- mkdocstrings 
- pre-commit 
- black 
- isort 
- mypy 
- flake8 
- pytest-asyncio 

Also, there is a lite version `git checkout lite`, without *tox, mkdocs, pre-commit and ci*.


## How to use
```shell
git clone https://github.com/dmitriiweb/template-project-python my-project
cd my-project
python update.py
make test
```
