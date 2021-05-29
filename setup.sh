#!/usr/bin/env bash
wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh
chmod +x Anaconda3-2020.07-Linux-x86_64.sh
./Anaconda3-2020.07-Linux-x86_64.sh -b -p ~/anaconda3
source ~/anaconda3/etc/profile.d/conda.sh
rm Anaconda3-2020.07-Linux-x86_64.sh
python3 -m pip install -r requirements.txt
