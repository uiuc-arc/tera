#!/usr/bin/env bash
# ./numpyro_setup.sh [dir]
if [ ! -e "numpyro/" ];then
    git clone https://github.com/uiuc-arc/numpyro.git
fi

source ~/anaconda3/etc/profile.d/conda.sh
conda create -n numpyro -y python=3.6
cd numpyro
git checkout before_1a1d21ffd2f4d42255a9e6c3a875cf3db687d997.sh
conda activate numpyro
conda install -y pip pytest
pip install -e ".[dev]"
conda deactivate
cd -
