# Python environment

## 1. install Anaconda

Go to [Anaconda](https://www.anaconda.com/download/#macos)
and install.

*   add `export PATH=~/anaconda3/bin:$PATH` to bash_rc/zshrc

## 2 virtual env

some useful command:

*   create env: `conda create -n yourenvname python=3.6`
*   clone env: `conda create --name myclone --clone myenv`
*   active env: `source activate yourenvname`
*   install package: `conda/pip install packages`
*   list virtual env: `conda info --envs`
*   remove env: `conda remove --name myenv --all`
*   export env: `conda env export > environment.yml`
*   recreate a env from yml file: `conda env create -f environment.yml`
*   update env: `conda env update`

Note:

- if you find that pip dependecy was not export by conda, then try to update your pip and conda: `conda update pip`, `conda update -n base conda`
