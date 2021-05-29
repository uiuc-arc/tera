#!/usr/bin/env bash
# ./parlai_setup.sh [dir]
cd $1
if [ -e "${1}/parlai" ];then
    echo "Already installed"
    exit 0
fi

source ~/anaconda3/etc/profile.d/conda.sh
conda create -n parlai python=3.6 -y
git clone https://github.com/uiuc-arc/ParlAI.git parlai
cd parlai
git checkout evalcommit
conda activate parlai
conda install -y pip pytest
pip install scipy==1.2.1 torch==1.4
python setup.py develop
conda deactivate
cd -
