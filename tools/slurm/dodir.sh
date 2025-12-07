#!/bin/bash
#
# Script to generate a run directory in $LOCALSCRATCH
#
# Use as
#
# ./dodirs.sh somename var d value
# 
# It will generate a director with name
# beginning with 'somename' and ending with a numerical string
# corresponding to the value assigned to the variable 'var'
# in the parameters.py file.
#
# Example:
#
# ./dodirs.sh run_Ek_ Ek e -5
#
# will generate directory named run_Ek_-5.0
# In each directory the file parameters.py
# will have the appropriate value assigned to the parameter Ek, the Ekman number,
# Ek =10**-5.0
# 
# If the argument 'e' is changed to 'd' then 'var' will have values
# that change linearly instead of as powers of ten. For example:
#
# ./dodirs.sh run_ricb_ ricb d 0.35
#
# will generate directories named run_ricb_0.35

pref=$1
var=$2
exp=$3
value=$4

folder=$pref$value

echo $folder $var=$value
	
mkdir $LOCALSCRATCH/$folder

cd $LOCALSCRATCH/$folder

cp -r $KORE_HOME/* . # copies the source files


# modify variables
sed -i 's,^\('$var'[ ]*=\).*,\1'$value',' bin/parameters.py	

sed -i 's,^\(dir=\).*,\1'$folder',' tools/slurm/subramp.sh