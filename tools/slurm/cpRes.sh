#!/bin/bash
#
# Script to copy result files from local scratch to global scratch
# Use as
# ./cpRes.sh folder
# 

dir=$1

# define global scratch destination
result_folder=$GLOBALSCRATCH/results/kore

# copy results back to global scratch
mkdir -p $result_folder/$dir

cp -r bin/parameters.py $result_folder/$dir/
cp -r *out* $result_folder/$dir/