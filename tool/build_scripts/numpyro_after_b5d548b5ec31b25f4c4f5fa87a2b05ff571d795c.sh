#!/usr/bin/env bash
# ./numpyro_setup.sh [dir]
if [ ! -e "numpyro/" ];then
    git clone https://github.com/uiuc-arc/numpyro.git
fi

source ~/anaconda3/etc/profile.d/conda.sh
conda create -n numpyro_after_b5d548b5ec31b25f4c4f5fa87a2b05ff571d795c -y python=3.6
cd numpyro
git checkout after_b5d548b5ec31b25f4c4f5fa87a2b05ff571d795c
conda activate numpyro_after_b5d548b5ec31b25f4c4f5fa87a2b05ff571d795c
conda install -y pip pytest
pip install -e ".[dev]"
pip install pyro-api
conda deactivate
cd -
