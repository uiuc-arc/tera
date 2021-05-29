#!/usr/bin/env bash
# ./numpyro_setup.sh [dir]
cd $1
if [ -e "${1}/numpyro" ];then
    echo "Already installed"
    exit 0
fi

source ~/anaconda3/etc/profile.d/conda.sh
conda create -n numpyro -y python=3.6
git clone https://github.com/uiuc-arc/numpyro.git
cd numpyro
if [ ! -z $2 ]; then
    # switch branch
    git checkout $2
else
    git checkout evalcommit
fi
conda activate numpyro
conda install -y pip pytest
pip install -r evalreqs.txt 
#pip install scipy==1.4.0
#pip install jax==0.2.2
pip install -e ".[dev,test]"
conda deactivate
cd -
