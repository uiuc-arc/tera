#!/usr/bin/env bash
# ./pyGPGO_setup.sh [dir]
cd $1
if [ -e "${1}/pyGPGO" ];then
    echo "Already installed"
    exit 0
fi

source ~/anaconda3/etc/profile.d/conda.sh
conda create -n pyGPGO python=3.6 -y

git clone https://github.com/uiuc-arc/pyGPGO.git
cd pyGPGO
git checkout evalcommit
conda activate pyGPGO
conda install -y pip pytest
pip install -r evalreqs.txt
pip uninstall -y theano
cd ../ 
git clone https://github.com/Theano/Theano.git
cd Theano
python setup.py install
cd ../pyGPGO

pip install numpy scipy joblib scikit-learn pymc3 theano
python setup.py install
#pip install -e .
conda deactivate
cd -
