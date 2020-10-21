package require cafe 1.0

mmpbsa -top ./openmm_simulation/complex_plus_water.parm7 -trj ./centred.dcd -out mmpbsa.log -top_type parm7 -com "protein or resname UNL" -rec "protein" -lig "resname UNL" -first 0 -last -1 -stride 1 -mm 1 -pb 2 -pb_exe apbs -pb_rad mparse -pb_bcfl mdh -sa 1 -sa_rad mparse -sa_gamma 0.00542 -sa_beta 0.92
    
