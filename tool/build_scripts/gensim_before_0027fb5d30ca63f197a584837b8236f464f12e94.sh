#!/usr/bin/env bash

source ~/anaconda3/etc/profile.d/conda.sh

conda create -n gensim python=3.6.3 -y
conda activate gensim
cd $1

if [ ! -e "gensim/" ] ;then
    git clone https://github.com/uiuc-arc/gensim.git
fi
cd gensim
git checkout before_0027fb5d30ca63f197a584837b8236f464f12e94
pip install -e ".[test]"
cd ..
conda deactivate