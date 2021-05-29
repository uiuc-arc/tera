#!/usr/bin/env bash

source ~/anaconda3/etc/profile.d/conda.sh

conda create -n pyGPGO_after_c21120ffd974029485877dcebafb2c0b930e1f16 python=3.6 -y
conda activate pyGPGO_after_c21120ffd974029485877dcebafb2c0b930e1f16

if [ ! -e "pyGPGO/" ] ;then
    git clone https://github.com/uiuc-arc/pyGPGO.git
fi

cd pyGPGO
git checkout after_c21120ffd974029485877dcebafb2c0b930e1f16
conda install -y pip pytest
pip install pymc3==3.5 scipy==1.1.0 theano==1.0.2 scikit-learn==0.19.2 numpy==1.15.0 pandas==0.23.4
pip install -e .
cd ..
conda deactivate