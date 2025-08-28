#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

# Load the summary file, skipping the header line
# Each line: Residue  Ext  Bridge  3-10  Alpha  Pi  Turn  Bend
data = []
with open('trial21.dssp.summary') as f:
    for line in f:
        if line.strip().startswith('#'):
            continue
        parts = line.split()
        # residue = int(parts[0])
        vals = list(map(float, parts[1:]))  # Ext, Bridge, 3-10, Alpha, Pi, Turn, Bend
        data.append(vals)

arr = np.array(data)  # shape: (n_residues, 7)

# Helix occupancy = columns 2 (3-10) + 3 (Alpha) + 4 (Pi)
helix = arr[:,2] + arr[:,3] + arr[:,4]

# Residue numbers from file: assume consecutive from first parsed line
first_res = None
with open('trial21.dssp.summary') as f:
    for line in f:
        if not line.strip().startswith('#'):
            first_res = int(line.split()[0])
            break
residues = np.arange(first_res, first_res + len(helix))

# Plot
plt.figure(figsize=(8,4))
plt.bar(residues, helix*100, color='teal')
plt.xlabel('Residue Number')
plt.ylabel('Helix Occupancy (%)')
plt.title('Trial 21 Helical Content per Residue')
plt.ylim(0,100)
plt.xticks(residues, rotation=45)
plt.tight_layout()
plt.show()

