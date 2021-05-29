#!/usr/bin/env bash

source ~/anaconda3/etc/profile.d/conda.sh
ENVS=$(conda env list | awk '{print $1}' )
if [[ $ENVS = *"gensim_after_3db9406a146c0ab0932353ae5b6a58b66838c631"* ]]; then
   conda activate gensim_after_3db9406a146c0ab0932353ae5b6a58b66838c631
else
    conda create -n gensim_after_3db9406a146c0ab0932353ae5b6a58b66838c631 python=3.6.3 -y
    conda activate gensim_after_3db9406a146c0ab0932353ae5b6a58b66838c631
fi

if [ ! -e "gensim/" ] ;then
    git clone https://github.com/uiuc-arc/gensim.git
fi
cd gensim
git checkout after_3db9406a146c0ab0932353ae5b6a58b66838c631
pip install -e ".[test]"
pip install nbformat nbconvert
cd ..
conda deactivate