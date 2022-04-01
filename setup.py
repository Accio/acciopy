from setuptools import setup, find_packages

setup(
    name="acciopy",
    version="0.1.0",
    author="Jitao David Zhang",
    author_email="jitao_david.zhang@roche.com",
    url="https://github.com/Accio/acciopy",
    scripts=[],
    packages=find_packages(),
    install_requires=['python-Levenshtein'],
    python_requires=">=3.7",
)
