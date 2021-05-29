#!/usr/bin/env bash

cd $1
if [ -e "${1}/pymc-learn" ];then
    echo "Already installed"
    exit 0
fi

source ~/anaconda3/etc/profile.d/conda.sh
conda create -n pymc-learn -y
git clone https://github.com/uiuc-arc/pymc-learn.git
cd pymc-learn
git checkout evalcommit
conda activate pymc-learn
conda install -y pip pytest
pip install -r evalreqs.txt 
pip install -r requirements-dev.txt
pip install -r requirements.txt
pip install -e .
conda deactivate
cd -
