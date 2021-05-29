#!/usr/bin/env bash
cd $1
if [ -e "${1}/gpytorch" ];then
    echo "Already installed"
    exit 0
fi

source ~/anaconda3/etc/profile.d/conda.sh
conda create -n gpytorch python=3.6 -y
git clone https://github.com/uiuc-arc/gpytorch.git gpytorch
cd gpytorch
#git checkout c3cb2621f0b0b58fe6ba5a5d34030d57980e20eb -b evalcommit
git checkout  evalcommit
conda activate gpytorch
conda install -y pip pytest

pip install -e ".[dev,test]"
conda deactivate
cd -