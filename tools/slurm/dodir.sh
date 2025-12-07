#!/bin/bash
#
# Script to generate a run directory in $LOCALSCRATCH
#
# Use as
#
# ./dodirs.sh folder var d value

folder=$1
var=$2
exp=$3
value=$4

echo $folder $var=$value
	
mkdir $LOCALSCRATCH/$folder

cd $LOCALSCRATCH/$folder

cp -r $KORE_HOME/* . # copies the source files


# modify variables
sed -i 's,^\('$var'[ ]*=\).*,\1'$value',' bin/parameters.py	