# mmpbsa_from_openmm
example demonstrating a free energy estimation starting from OFF and OpenMM

# how to do:

- [x] process PDB (1XEP - catechol bound to T4 lysozyme) file with openmm-setup
- [x] in `align_ligand.ipynb`, generate an RDKit `mol` object that is aligned
with the crystal structure ligand
- [x] in `parameterize_ligand.ipynb`, use OpenForceField to parameterize this `mol`
object - also save a drug prmtop for later analysis.
- [x] in `combine_systems.ipynb`, add the parameterized ligand to the system and save.
- [ ] individually save prmtop files for the complex and the receptor alone (for MMPBSA analysis).
