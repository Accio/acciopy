# davidpy: my python snippets

See [tutorial of packaging
projects](https://packaging.python.org/tutorials/packaging-projects/).

1. Put source files in modules under `src`, including `__init__.py` files.
1. Create `pyproject.toml`, `README.md`, and `setup.cfg` files.
1. Setup testpy token

```bash
## building
python3 -m pip install --upgrade build
python3 -m build

## uploading to testpypi
python3 -m pip install --upgrade twine
python3 -m twine upload --repository testpypi dist/*

## installation
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps
davidpy-Accio
```

## fuzzmatch_filenames

A simple module to fuzzy-match two lists of file names.

