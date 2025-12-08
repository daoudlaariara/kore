#!/bin/bash
#
# Script to run Kore simulations on a SLURM-managed cluster
# with a variable parameter.
#
# Call : sbatch --array 0-<num> ./srunKore.sh somename var d startvalue step
# 
# Example calls: 
#   sbatch --array 0-10 ./srunKore.sh run_ricb_ ricb d 0.3 0.1
#   sbatch --array 0-10 ./srunKore.sh run_Ek_ Ek e -5 -0.1
#
# Where --array can be specified in the sbatch or change in the file
#
# Also possible to make a simple run : sbatch ./srunKore.sh, with the current parameter file
# 
#SBATCH --job-name=kore
#SBATCH --output=output.txt
#
#SBATCH --time=10:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem-per-cpu=2000

#------------------------------------------------------------------------------------------------------  
#------------------------------------------------------------------------------------------------------  

#---------- Options -----------------------------------------------------------------------------------
#### For forced problems use:
### for simple test problems
export opts='-ksp_type preonly -pc_type lu'
#export opts='-ksp_type preonly -pc_type lu -pc_factor_mat_solver_type superlu_dist -ksp_monitor -ksp_converged_reason'
### use for standard problems with mumps (fast but requires more memory) amd an iterative solver (less memory but no guaranteed convergence)
#export opts='-ksp_type gmres -pc_type lu -pc_factor_mat_solver_type mumps -ksp_monitor_true_residual -ksp_monitor -ksp_converged_reason'
### use for standard problems with mumps (fast but requires more memory) and a direct solver (more memory)
#export opts='-ksp_type preonly -pc_type lu -pc_factor_mat_solver_type mumps -ksp_monitor_true_residual -ksp_monitor -ksp_converged_reason'
### use for standard problems with superlu dist (should always work)
#export opts='-ksp_type preonly -pc_type lu -pc_factor_mat_solver_type superlu_dist -ksp_monitor -ksp_converged_reason -mat_superlu_dist_iterrefine 1 -mat_superlu_dist_colperm PARMETIS -mat_superlu_dist_parsymbfact 1'
### use for induction problems
#export opts='-ksp_type preonly -pc_type lu -pc_factor_mat_solver_type superlu_dist -ksp_monitor -ksp_converged_reason -mat_superlu_dist_iterrefine 1 -mat_superlu_dist_colperm PARMETIS'
#------------------------------------------------------------------------------------------------------  
#------------------------------------------------------------------------------------------------------  
### For eigenvalue problems use:
#export opts='-st_type cayley -eps_error_relative ::ascii_info_detail'
#export opts='-st_type sinvert -eps_error_relative ::ascii_info_detail'
#export opts='-st_type sinvert -eps_error_relative ::ascii_info_detail -eps_balance oneside -pc_factor_mat_solver_type mumps -mat_mumps_icntl_14 300'
#export opts='-st_type sinvert -eps_error_relative ::ascii_info_detail -pc_factor_mat_solver_type mumps -mat_mumps_icntl_14 1000 -mat_mumps_icntl_23 8000'
#export opts='-st_type sinvert -st_ksp_type preonly -st_pc_type lu -st_pc_factor_mat_solver_type superlu_dist'
#export opts='-st_type sinvert -st_ksp_type preonly -st_pc_type lu -st_pc_factor_mat_solver_type superlu_dist'
#export opts='-st_type sinvert -st_ksp_type preonly -st_pc_type lu -eps_error_relative ::ascii_info_detail -st_pc_factor_mat_solver_type superlu_dist -mat_superlu_dist_iterrefine 1 -mat_superlu_dist_colperm PARMETIS -mat_superlu_dist_parsymbfact 1'
#export opts='-st_type sinvert -st_pc_factor_mat_solver_type mumps -mat_mumps_icntl_14 3000 -eps_true_residual -eps_converged_reason -eps_conv_rel -eps_monitor_conv -eps_error_relative ::ascii_info_detail -eps_balance twoside'

ncpus=$SLURM_CPUS_PER_TASK
#------------------------------------------------------------------------------------------------------  
#------------------------------------------------------------------------------------------------------

# Check number of arguments
if [ $# -eq 0 ]; then
    sed -i 's,^\('ncpus'[ ]*=\).*,\1'$ncpus',' bin/parameters.py	

    folder="run_default"

elif [ $# -eq 5 ]; then
    pref=$1
    var=$2
    exp=$3
    startvalue=$4
    step=$5

    k=$(echo "$startvalue + ($SLURM_ARRAY_TASK_ID * $step)" | bc | awk '{printf "%f", $0}')
    if [ "$exp" = 'e' ]; then
            value='10**'$k # powers of ten
    else
        value=$k # linear
    fi
    #------------------------------------------------------------------------------------------------------  
    #------------------------------------------------------------------------------------------------------  

    # Create the run directories
    folder=$pref$value
    echo $folder $var=$value
    mkdir $LOCALSCRATCH/$folder
    cd $LOCALSCRATCH/$folder
    cp -r $KORE_HOME/* . # copies the source files

    # modify variables
    sed -i 's,^\('$var'[ ]*=\).*,\1'$value',' bin/parameters.py	
    sed -i 's,^\('ncpus'[ ]*=\).*,\1'$ncpus',' bin/parameters.py	

    srun sleep 0.2
else
    echo "Wrong number of arguments. Either none or five arguments are required."
    exit 1
fi


# Run the simulations
srun ./bin/submatrices.py $ncpus >> out0
srun ./bin/assemble.py >> out1
srun ./bin/solve.py $opts >> out2
srun ./bin/spin_doctor.py $ncpus >> out3

# Copy results back to global scratch
# define global scratch destination
result_folder=$GLOBALSCRATCH/results/kore

# copy results back to global scratch
mkdir -p $result_folder/$folder

cp -r bin/parameters.py $result_folder/$folder/
cp -r *out* $result_folder/$folder/
cp -r *.dat $result_folder/$folder/

rm *.field
rm *.npz
rm *.mtx
rm *.dat
rm *out*