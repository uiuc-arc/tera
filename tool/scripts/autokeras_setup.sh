#!/usr/bin/env bash
# ./autokeras_setup.sh [dir]
cd $1
if [ -e "${1}/autokeras" ];then
echo "Already installed"
    exit 0
fi

source ~/anaconda3/etc/profile.d/conda.sh
conda create -n autokeras -y python=3.6
git clone https://github.com/uiuc-arc/autokeras.git
cd autokeras
if [ ! -z $2 ]; then
    # switch branch
    git checkout $2
else
    git checkout evalcommit
fi
#git checkout evalcommit
conda activate autokeras
conda install -y pip pytest #p ytest pytest-cov pytest-xdist pytest-timeout
pip install -r evalreqs.txt
pip install tensorflow==2.2.0
pip install git+https://github.com/keras-team/keras-tuner.git@1.0.2rc1
#pip3 install autokeras==1.0.5
pip install -e ".[tests]"
#pip uninstall autokeras
pip install mkdocs
pip install mkdocs-material
pip install autopep8
pip install git+https://github.com/gabrieldemarmiesse/typed_api.git@0.1.1

conda deactivate
cd -
