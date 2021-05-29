#!/usr/bin/env bash

source ~/anaconda3/etc/profile.d/conda.sh
ENVS=$(conda env list | awk '{print $1}' )
if [[ $ENVS = *"sbi_after_c8aec2f86046812f3bc053a9bff5c57d485e495c"* ]]; then
    conda activate sbi_after_c8aec2f86046812f3bc053a9bff5c57d485e495c
else
    conda create -n sbi_after_c8aec2f86046812f3bc053a9bff5c57d485e495c python=3.7 -y
    conda activate sbi_after_c8aec2f86046812f3bc053a9bff5c57d485e495c
fi
if [ ! -e "sbi/" ] ;then
    git clone https://github.com/uiuc-arc/sbi.git
fi

cd sbi
git checkout after_c8aec2f86046812f3bc053a9bff5c57d485e495c
conda install -y pip pytest
pip install -e .
pip install pytorch-lightning==0.9.0
pip install sklearn
cd ..
conda deactivate