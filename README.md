# mmpbsa_from_openmm
example demonstrating a free energy estimation starting from OFF and OpenMM

# how to do:

- [x] process PDB file with openmm-setup
- [x] in align_ligand.ipynb, generate an RDKit `mol` object that is aligned with the crystal structure ligand
- [ ] use OpenForceField to parameterize this `mol` object
- [ ] add the parameterized ligand to the system.
- [ ] individually save prmtop files for complex, receptor alone, and ligand alone (this is for analysis later).
