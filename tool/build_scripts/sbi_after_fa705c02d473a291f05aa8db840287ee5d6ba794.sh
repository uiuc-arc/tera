#!/usr/bin/env bash
# ./sbi_setup.sh [dir]
if [ ! -e "/sbi" ];then
    git clone https://github.com/uiuc-arc/sbi.git sbi
fi

source ~/anaconda3/etc/profile.d/conda.sh
conda create -n sbi_after_fa705c02d473a291f05aa8db840287ee5d6ba794 -y
cd sbi
git checkout after_fa705c02d473a291f05aa8db840287ee5d6ba794
conda activate sbi_after_fa705c02d473a291f05aa8db840287ee5d6ba794
conda install -y pip pytest
pip install torch
pip install -e ".[dev]"
conda deactivate
cd -
