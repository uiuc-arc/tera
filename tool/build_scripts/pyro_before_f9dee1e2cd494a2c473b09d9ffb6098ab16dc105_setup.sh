#!/usr/bin/env bash
# ./pyro_before_f9dee1e2cd494a2c473b09d9ffb6098ab16dc105 [dir]

if [ ! -e "pyro/" ];then
    git clone https://github.com/uiuc-arc/pyro.git 
fi

source ~/anaconda3/etc/profile.d/conda.sh
conda create -n pyro python=3.5.6 -y
cd pyro
git checkout before_f9dee1e2cd494a2c473b09d9ffb6098ab16dc105
conda activate pyro
conda install -y pip pytest
pip install https://github.com/pyro-ppl/pyro-api/archive/master.zip
pip install torch==1.5.0 torchvision==0.6.0 -f https://download.pytorch.org/whl/torch_stable.html
pip install coveralls
pip install .
conda deactivate
cd -
