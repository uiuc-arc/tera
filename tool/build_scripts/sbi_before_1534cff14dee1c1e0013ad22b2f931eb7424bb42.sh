#!/usr/bin/env bash

source ~/anaconda3/etc/profile.d/conda.sh
ENVS=$(conda env list | awk '{print $1}' )
if [[ $ENVS = *"sbi_before_1534cff14dee1c1e0013ad22b2f931eb7424bb42"* ]]; then
    conda activate sbi_before_1534cff14dee1c1e0013ad22b2f931eb7424bb42
else
    conda create -n sbi_before_1534cff14dee1c1e0013ad22b2f931eb7424bb42 python=3.7 -y
    conda activate sbi_before_1534cff14dee1c1e0013ad22b2f931eb7424bb42
fi
if ! [ -e "sbi/" ] ;then
    git clone https://github.com/uiuc-arc/sbi.git
fi

cd sbi
git checkout before_1534cff14dee1c1e0013ad22b2f931eb7424bb42
conda install -y pip pytest
pip install -e .
pip install pytorch-lightning==0.9.0
pip install sklearn
cd ..
conda deactivate