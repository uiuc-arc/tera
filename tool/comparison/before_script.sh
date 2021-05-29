#!/bin/bash
cd ..
FILENAME=$(find . -name 'testspec_'"$2"'*.py')
cp $FILENAME testspecs.py
if ![ -e "./${1}" ];then
    bash '../tool/scripts/'"$1"'_setup.sh' ./
fi
FILENAME=$(find . -name '*'"$2"'*')
cd ../projects/
bash '../tool/'"$FILENAME"
python ../tool/optimizer.py -r $1 -t $3
cd $1
pytest -k $3