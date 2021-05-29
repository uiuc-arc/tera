#!/usr/bin/env bash
# ./fairseq_setup.sh [dir]
cd $1
if [ -e "${1}/fairseq" ];then
    echo "Already installed"
    exit 0
fi

source ~/anaconda3/etc/profile.d/conda.sh
conda create -n fairseq python=3.6 -y
git clone https://github.com/uiuc-arc/fairseq.git
cd fairseq
#git checkout ffecb4e3496379edf5ecae1483df5b7e0886c264 -b evalcommit
git checkout evalcommit
conda activate fairseq
conda install -y pip pytest
pip install torch
pip install --editable ./
conda deactivate
cd -
