#!/bin/bash
#
# Script to run Kore simulations on a SLURM-managed cluster
# with a variable parameter.
#
# Call : ./tools/slurm/runsKore.sh somename var d startvalue step endvalue
# 
#SBATCH --job-name=kore
#SBATCH --output=array_%A_%a.out
#SBATCH --error=array_%A_%a.err
#
#SBATCH --time=10:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=1000
#
#SBATCH --array=0-3

pref=$1
var=$2
exp=$3
startvalue=$4
step=$5
endvalue=$6

k=$(echo "$startvalue + ($SLURM_ARRAY_TASK_ID * $step)" | bc)
if [ "$exp" = 'e' ]; then
        value='10**'$k # powers of ten
else
    value=$k # linear
fi

# Create the run directories
folder=$pref$value
srun ./tools/slurm/dodir.sh $folder $var $exp $value
cd $LOCALSCRATCH/$folder

# Run the simulations
#srun sleep 0.2
srun ./tools/slurm/runKore.sh $SLURM_CPUS_PER_TASK
#rm *.field
rm *.npz
rm *.mtx

# Copy results back to global scratch
srun ./tools/slurm/cpRes.sh $folder