# Python environment

## 1. install Anaconda

Go to [Anaconda](https://www.anaconda.com/download/#macos)
and install.

*   add `export PATH=~/anaconda3/bin:$PATH` to bash_rc/zshrc
*   create env: `conda create -n myenv python=3.6`
*   check virtual env: `conda info --envs`
*   remove env: `conda remove --name myenv --all`
