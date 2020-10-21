# mmpbsa_from_openmm
example demonstrating a free energy estimation starting from OpenFoceField-parameterized ligands and OpenMM-derived
trajectory. 

# file prep:
see files in `openmm_simulation` dir.

- [x] process PDB (1XEP - catechol bound to T4 lysozyme) file with openmm-setup
- [x] in `align_ligand.ipynb`, generate an RDKit `mol` object that is aligned
with the crystal structure ligand
- [x] in `parameterize_ligand.ipynb`, use OpenForceField to parameterize this `mol`
object - also save a drug prmtop for later analysis.
- [x] in `combine_systems.ipynb`, add the parameterized ligand to the system and save.
- [x] in 'save_protein_and_complex_prmtop`, individually save prmtop files for the
complex, and for the receptor alone (for MMPBSA analysis).


You now have a `.parm7` file called `complex_plus_water.parm7`. There will also be `complex_system.xml`,
which is an openmm `System` object that can be fed into a `Simulation` to make a trajectory.
Thus we have the building blocks for an MMPBSA in CaFE in VMD.

# generate a trajectory

- [x] in the top directory, see `generate_trajectory.ipynb` to generate a trajectory using OpenMM

# analyse

- [x] run VMD script (`vmd -dispdev text < analyse.tcl > out.log`), having installed APBS, NAMD2
and CaFE plugin.

# tidbits

- CaFE can be installed by cloning the CaFE repo at https://github.com/HuiLiuCode/CaFE_Plugin,
then changing the name of the `src` dir within to `cafe1.0`. To let VMD know where this directory is,
add this line to your ~/.vmdrc file (change the actual filepath to your own computer):
`set auto_path [linsert $auto_path 0 {/home/lewis/Documents/cafe/cafe1.0}]`
- Test if CaFE runs by opening vmd and typing `package require cafe 1.0`
- You will need to install `APBS` and add it to the PATH so it can be called from within CaFE
- APBS is offered as a binary and, to run it, you will need to add the `lib` dir within the APBS
directory to the LD_LIBRARY_PATH as well
- Likewise you need to install `namd2` and add it to the PATH
- CaFE script uses the defaults from the manual. Up to you whether that applies in every case.
- APBS takes a long time to run even with 8CPUs. 250 frames took 40 minutes.
