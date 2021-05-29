#!/usr/bin/env bash
# ./sbi_setup.sh [dir]
cd $1
if [ -e "${1}/sbi" ];then
    echo "Already installed"
    exit 0
fi

source ~/anaconda3/etc/profile.d/conda.sh
conda create -n sbi -y python=3.7
git clone https://github.com/uiuc-arc/sbi.git
cd sbi
git checkout evalcommit
conda activate sbi
conda install -y pip pytest
pip install torch
pip install -e ".[dev]"
conda deactivate
cd -
