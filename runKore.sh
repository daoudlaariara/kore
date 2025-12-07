#!/bin/bash

ncpus=$1

opts='-st_type sinvert -eps_error_relative ::ascii_info_detail'
#opts='-ksp_type preonly -pc_type lu'

./bin/submatrices.py $ncpus
mpiexec -n $ncpus ./bin/assemble.py
mpiexec -n $ncpus ./bin/solve.py $opts
#./postprocess.py
