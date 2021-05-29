#!/usr/bin/env bash
# ./ml-agents_3f4b2b59cff8038bc6f25550e39296e2cc8695cb_setup.sh [dir]

if [ ! -e "ml-agents/" ];then
    git clone https://github.com/uiuc-arc/ml-agents.git 
fi

source ~/anaconda3/etc/profile.d/conda.sh
conda create -n ml-agents python=3.7 -y
cd ml-agents
git checkout before_3f4b2b59cff8038bc6f25550e39296e2cc8695cb
conda activate ml-agents
conda install -y pip pytest
pip3 install torch -f https://download.pytorch.org/whl/torch_stable.html
pip3 install -e ./ml-agents-envs
pip3 install -e ./ml-agents
conda deactivate
cd -
