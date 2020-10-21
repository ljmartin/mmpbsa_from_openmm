# mmpbsa_from_openmm
example demonstrating a free energy estimation starting from OFF and OpenMM

# file prep:
see in `openmm_simulation` dir.

- [x] process PDB (1XEP - catechol bound to T4 lysozyme) file with openmm-setup
- [x] in `align_ligand.ipynb`, generate an RDKit `mol` object that is aligned
with the crystal structure ligand
- [x] in `parameterize_ligand.ipynb`, use OpenForceField to parameterize this `mol`
object - also save a drug prmtop for later analysis.
- [x] in `combine_systems.ipynb`, add the parameterized ligand to the system and save.
- [x] in 'save_protein_and_complex_prmtop`, individually save prmtop files for the
complex, and for the receptor alone (for MMPBSA analysis).


You know have `drug.prmtop`, `receptor.prmtop`, and `complex.prmtop`. There will also be `complex_system.xml`,
which is an openmm `System` object that can be run to make a trajectory. Thus we have the building blocks
for an MMPBSA calculation using either MMPBSA.py from the AMBER toolkit, or CaFE in VMD.

# generate a trajectory

