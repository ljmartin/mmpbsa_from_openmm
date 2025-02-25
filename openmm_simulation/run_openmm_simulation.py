# This script was generated by OpenMM-Setup on 2020-10-21.

from simtk.openmm import *
from simtk.openmm.app import *
from simtk.unit import *

# Input Files

pdb = PDBFile('1xep-processed.pdb')
forcefield = ForceField('amber14-all.xml', 'amber14/tip3p.xml')

# System Configuration

nonbondedMethod = CutoffNonPeriodic
nonbondedCutoff = 2.0*nanometers
constraints = HBonds
rigidWater = True
constraintTolerance = 0.000001

# Integration Options

dt = 0.002*picoseconds
temperature = 300*kelvin
friction = 1.0/picosecond

# Simulation Options

steps = 1000000
equilibrationSteps = 1000
platform = Platform.getPlatformByName('CUDA')
platformProperties = {'Precision': 'single'}
dcdReporter = DCDReporter('trajectory.dcd', 10000)
dataReporter = StateDataReporter('log.txt', 1000, totalSteps=steps,
    step=True, speed=True, progress=True, potentialEnergy=True, temperature=True, separator='\t')
checkpointReporter = CheckpointReporter('checkpoint.chk', 10000)

# Prepare the Simulation

print('Building system...')
topology = pdb.topology
positions = pdb.positions
system = forcefield.createSystem(topology, nonbondedMethod=nonbondedMethod, nonbondedCutoff=nonbondedCutoff,
    constraints=constraints, rigidWater=rigidWater)
integrator = LangevinIntegrator(temperature, friction, dt)
integrator.setConstraintTolerance(constraintTolerance)
simulation = Simulation(topology, system, integrator, platform, platformProperties)
simulation.context.setPositions(positions)

# Minimize and Equilibrate

print('Performing energy minimization...')
simulation.minimizeEnergy()
print('Equilibrating...')
simulation.context.setVelocitiesToTemperature(temperature)
simulation.step(equilibrationSteps)

# Simulate

print('Simulating...')
simulation.reporters.append(dcdReporter)
simulation.reporters.append(dataReporter)
simulation.reporters.append(checkpointReporter)
simulation.currentStep = 0
simulation.step(steps)