# Python environment

## 1. install Anaconda

Go to [Anaconda](https://www.anaconda.com/download/#macos)
and install.

*   add `export PATH=~/anaconda3/bin:$PATH` to bash_rc/zshrc

## 2 virtual env

some useful command:

*   create env: `conda create -n yourenvname python=3.6`
*   active env: `activate yourenvname`
*   check virtual env: `conda info --envs`
*   remove env: `conda remove --name myenv --all`
*   export env: `conda env export > environment.yml`
*   recreate a env from yml file: `conda env create -f environment.yml`
