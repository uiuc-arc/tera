#!/usr/bin/env bash

cd $1
if [ -e "${1}/pymc3" ];then
    echo "Already installed"
    exit 0
fi

source ~/anaconda3/etc/profile.d/conda.sh
conda create -n pymc3 -y python=3.7
git clone https://github.com/uiuc-arc/pymc3.git
cd pymc3
git checkout wseed
conda activate pymc3
conda install -y pip
sudo apt-get install -y libfreetype6-dev pkg-config
pip install -r evalreqs.txt
#pip install  pytest==5.0.0
pip install -r requirements-dev.txt
pip install -r requirements.txt
pip install -e .
#pip install matplotlib==2.2.0
conda deactivate
cd -
