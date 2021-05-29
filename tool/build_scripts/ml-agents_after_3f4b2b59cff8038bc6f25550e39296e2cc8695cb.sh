#!/usr/bin/env bash
# ./ml-agents_3f4b2b59cff8038bc6f25550e39296e2cc8695cb_setup.sh [dir]
if [ ! -e "ml-agents/" ];then
    git clone https://github.com/uiuc-arc/ml-agents.git 
fi

source ~/anaconda3/etc/profile.d/conda.sh
conda create -n ml-agents_after_3f4b2b59cff8038bc6f25550e39296e2cc8695cb python=3.7 -y
cd ml-agents
git checkout after_3f4b2b59cff8038bc6f25550e39296e2cc8695cb
conda activate ml-agents_after_3f4b2b59cff8038bc6f25550e39296e2cc8695cb
conda install -y pip
pip install pytest==5.3.2
pip install gym gym_unity==0.24.1
pip install torch -f https://download.pytorch.org/whl/torch_stable.html
pip install -e ./ml-agents-envs
pip install -e ./ml-agents
conda deactivate
cd -
