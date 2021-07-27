#!/bin/bash

rm -rf dist/*

# python3 -m pip install --upgrade build
python3 -m build

## uploading to testpypi
# python3 -m pip install --upgrade twine
python3 -m twine upload --repository testpypi dist/*

## installation
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps acciopy-Accio

