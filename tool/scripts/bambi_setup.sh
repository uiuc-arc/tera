#!/usr/bin/env bash
# ./bambi_setup.sh [dir]
cd $1
if [ -e "${1}/bambi" ];then
    echo "Already installed"
    exit 0
fi

source ~/anaconda3/etc/profile.d/conda.sh
conda create -n bambi python=3.7.7 -y
git clone https://github.com/uiuc-arc/bambi.git
cd bambi
git checkout evalcommit
conda activate bambi
conda install -y pip pytest
pip install -r evalreqs.txt
pip install arviz==0.10.0
pip install -r requirements.txt
pip install -e .
conda deactivate
cd -
