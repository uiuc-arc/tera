#!/usr/bin/env bash

source ~/anaconda3/etc/profile.d/conda.sh

conda create -n pyGPGO python=3.7 -y
conda activate pyGPGO

if [ ! -e "pyGPGO/" ] ;then
    git clone https://github.com/uiuc-arc/pyGPGO.git
fi

cd pyGPGO
git checkout before_1c718d7f2bdb95d407b27412b25471c762355832
conda install -y pip pytest
pip install pymc3==3.2 scipy==1.1.0
pip install -e .
cd ..
conda deactivate