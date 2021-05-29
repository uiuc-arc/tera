#!/usr/bin/env bash
# execute the original test suite
# ./mutation.sh [repo] [parallel cores] [mode==all,eval,opt] [timeout]

# by default it should be in evalcommit
random=$RANDOM
cores=30
mode="all"
tout=""
runs=1
if [ ! -z $2 ]; then
  cores=$2
fi

if [ ! -z $3 ]; then
  mode=$3
fi

if [ ! -z $4 ]; then
  tout="--timeout $4"
  echo $tout
fi

mkdir -p logs
mkdir -p ../projects

# install project if not installed yet
if [ ! -e ../projects/$1 ]; then
  echo ">>Installing $1 ..."
  ./scripts/${1}_setup.sh $(realpath ../projects)
fi

# install other dependencies
source ~/anaconda3/etc/profile.d/conda.sh
conda activate $1
which pip
echo ">>Installing requirements ..."
pip install mutmut==2.1.0 pytest-cov pytest-xdist pytest-timeout astunparse pandas shutils &>install.txt
conda deactivate
conda activate $1
if [ -e test_optimized/${1}.txt ]; then
  pytest_str=$(cat test_optimized/${1}.txt)
else
  pytest_str=$(python3 mutation.py $1)
fi

echo "Using tests: ${pytest_str}"
cd ../projects/$1
# clean folder
rm -rf .mut* mut* html*

git checkout -- .
git checkout evalcommit
# compute coverage
echo ">> Computing coverage ..."
pytest --cov=. -n $cores -W ignore ${pytest_str} &> coverage.txt
echo ">>Running mutation tests on original tests ... "
if [[ "$mode" == "all" || "$mode" == "eval" ]]; then
  for i in `seq 1 5`; do
  if [[ $cores == 1 ]]; then
    mutmut run --use-coverage --runner "pytest -x $tout ${pytest_str}" | tee -i mutmut_log_original.txt 2> /dev/null
  else
    mutmut run --use-coverage --runner "pytest -n $cores -x $tout ${pytest_str}" | tee -i mutmut_log_original.txt 2> /dev/null
  fi
  done
  echo ">>Done, generating results ..."
  mutmut results > mutation_results_original.txt
  mutmut html
  mv .mutmut-cache .mutmut-cache-original
  mv html html-original
fi

# switch to optimized tests branch
git checkout -- .
git checkout optimized

echo ">>Running mutation tests on optimized tests ... "
if [[ "$mode" == "all" || "$mode" == "opt" ]]; then
  for i in `seq 1 5`; do
  if [[ $cores == 1 ]]; then
    mutmut run --use-coverage --runner "pytest  -x -W ignore $tout ${pytest_str}" | tee -i mutmut_log_optimized.txt 2> /dev/null
  else
    mutmut run --use-coverage --runner "pytest -n $cores -x -W ignore $tout ${pytest_str}" | tee -i mutmut_log_optimized.txt 2> /dev/null
  fi
  done
  echo ">>Done, generating results ..."
  mutmut results >mutation_results_optimized.txt
  mutmut html
  mv .mutmut-cache .mutmut-cache-optimized
  mv html html-optimized
fi

# revert back the branch
git checkout -- .
git checkout evalcommit

outputdir='../../tool/logs/mut_${1}_${random}'
mkdir -p ../../tool/logs/mut_${1}_${random}
mv  .mutmut* mutmut* mutation_results* html* ../../tool/logs/mut_${1}_${random}
echo ">> Done! Output in `realpath ../../tool/logs/mut_${1}_${random}`"
