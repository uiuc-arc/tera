#!/usr/bin/env bash
envname=$1
source ~/anaconda3/etc/profile.d/conda.sh
name=`echo $envname | cut -d"_" -f2-`
mkdir -p test_logs/
touch test_logs/${name}.txt
logpath=`realpath test_logs/${name}.txt`
conda activate ${envname}
cd ~/projects/borntobeflaky/projects/pytorch-deps/$name
pytest -q --collect-only . > ${logpath}
conda deactivate
cd -



