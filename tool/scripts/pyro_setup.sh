#!/usr/bin/env bash

cd $1
if [ -e "${1}/pyro" ];then
    echo "Already installed"
    exit 0
fi

source ~/anaconda3/etc/profile.d/conda.sh
conda create -n pyro -y python=3.6
git clone https://github.com/uiuc-arc/pyro.git
cd pyro
git checkout evalcommit
conda activate pyro
conda install -y pip pytest
pip install torch==1.4.0+cpu torchvision==0.5.0+cpu -f https://download.pytorch.org/whl/torch_stable.html
pip uninstall -y pytest
pip install -r evalreqs.txt
pip install -e ".[dev,extras,test]"
conda deactivate
cd -
