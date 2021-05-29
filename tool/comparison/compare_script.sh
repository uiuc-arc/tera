#!/usr/bin/env bash
cd ..
source ~/anaconda3/etc/profile.d/conda.sh
cd build_scripts/
FILENAME=$(find . -name '*'"after_$2"'*')
cd ../../projects/
envn=`conda env list | grep $2 | wc -l`
if [[ $envn -eq 0 ]];then
       echo "Creating conda env..."
       bash '../tool/build_scripts/'"$FILENAME"
else
       echo "Found conda env"
fi

IFS='/' read -ra ADDR <<< "$FILENAME"
FILENAME=${ADDR[1]}
IFS='.' read -ra ADDR <<< "$FILENAME"
CONDA_ENV=${ADDR[0]}
conda activate $CONDA_ENV
cd $1
git checkout after_$2
pytest $3 &> res_after.txt
git checkout opt_$2
pytest $3 &> res_opt.txt
failed_after=`grep failed res_after.txt | wc -l`
failed_opt=`grep failed res_opt.txt | wc -l`
if [ ${failed_after} -ge 1 ] && [ ${failed_opt} -ge 1 ]; then
  echo "Success. Both tests fail"
  echo "Passed" > result_${2}.txt
else
  echo "Failed. Both tests dont fail"
  echo "Failed" > result_${2}.txt
fi
git checkout evalcommit &> /dev/null
