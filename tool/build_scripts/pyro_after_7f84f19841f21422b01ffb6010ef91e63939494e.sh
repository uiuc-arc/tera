#!/usr/bin/env bash
# ./pyro_after_7f84f19841f21422b01ffb6010ef91e63939494e [dir]

if [ ! -e "pyro/" ];then
    git clone https://github.com/uiuc-arc/pyro.git
fi

source ~/anaconda3/etc/profile.d/conda.sh
conda create -n pyro_after_7f84f19841f21422b01ffb6010ef91e63939494e python=3.7 -y
cd pyro
git checkout after_7f84f19841f21422b01ffb6010ef91e63939494e
conda activate pyro_after_7f84f19841f21422b01ffb6010ef91e63939494e
conda install -y pip pytest
pip install scipy
pip install -e .
conda deactivate
cd -
