#!/usr/bin/env bash
# ./ml-agents_setup.sh [dir]
cd $1
if [ -e "${1}/ml-agents" ];then
    echo "Already installed"
    exit 0
fi

source ~/anaconda3/etc/profile.d/conda.sh
conda create -n ml-agents -y python=3.6
git clone https://github.com/uiuc-arc/ml-agents.git
cd ml-agents
#git checkout cb44d9be5321d18f6ccddc3595f366bb06e3064f -b evalcommit
git checkout evalcommit
conda activate ml-agents
conda install -y pip pytest
pip install -e ./ml-agents-envs
pip install -e ./ml-agents
conda deactivate
cd -