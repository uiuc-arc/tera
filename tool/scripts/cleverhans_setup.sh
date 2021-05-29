#!/usr/bin/env bash
# ./cleverhans_setup.sh [dir]
cd $1
if [ -e "${1}/cleverhans" ]; then
  echo "Already installed"
  exit 0
fi


source ~/anaconda3/etc/profile.d/conda.sh
conda create -n cleverhans python=3.6 -y
git clone https://github.com/uiuc-arc/cleverhans.git
cd cleverhans
git checkout  evalcommit

conda activate cleverhans
conda install -y pip pytest
pip install https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.12.0rc1-cp36-cp36m-linux_x86_64.whl
pip install torch==1.0.1.post2 torchvision==0.2.2 -q
pip install scipy==1.4.0
pip install google-cloud==0.33.1
pip install tensorflow_addons
pip install nose
#pip install torch tensorflow==1.14
python setup.py install
conda deactivate
