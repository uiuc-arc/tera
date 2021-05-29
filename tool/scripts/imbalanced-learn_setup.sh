#!/usr/bin/env bash
# ./imbalanced-learn_setup.sh [dir]
cd $1
if [ -e "${1}/imbalanced-learn" ];then
    echo "Already installed"
    exit 0
fi

source ~/anaconda3/etc/profile.d/conda.sh
conda create -n imbalanced-learn python=3.7 -y
git clone https://github.com/uiuc-arc/imbalanced-learn.git
cd imbalanced-learn
git checkout evalcommit
conda activate imbalanced-learn
conda install -y pip pytest
pip install scipy numpy scikit-learn==0.23 joblib tensorflow
pip install -e .
conda deactivate
cd -


