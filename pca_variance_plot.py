#!/usr/bin/env python3
import mdtraj as md
import numpy as np
import matplotlib.pyplot as plt
import sys

# Edit these to your filenames
topology = "clean_6mdx_sol.prmtop"
trajfile = "mdcrd.nc"

# Load trajectory (mdtraj supports netcdf if built with netcdf4)
traj = md.load(trajfile, top=topology)

# Select backbone atoms N, C, CA (same mask you used in cpptraj)
# mdtraj selection: atom name selectors are case-sensitive
sel = traj.topology.select("name N or name CA or name C")
if sel.size == 0:
    print("WARNING: selection empty. Check atom names in topology.")
    sys.exit(1)

traj_bb = traj.atom_slice(sel)

# Align to the first frame (superpose removes global translation/rotation)
traj_bb.superpose(traj_bb, 0)

# Flatten coordinates: n_frames x (3 * n_atoms)
X = traj_bb.xyz.reshape(traj_bb.n_frames, -1)

# Subtract mean (centering)
Xc = X - X.mean(axis=0)

# Covariance matrix of coordinates (columns are coordinate dims)
C = np.cov(Xc, rowvar=False)   # shape: (3*n_atoms, 3*n_atoms)

# Eigen decomposition (use eigh for symmetric)
eigvals, eigvecs = np.linalg.eigh(C)

# Sort eigenvalues descending
idx = eigvals.argsort()[::-1]
eigvals = eigvals[idx]

# Convert to variance percentages
eigvar = eigvals / np.sum(eigvals) * 100.0
cumulative = np.cumsum(eigvar)

# Print first 20 PCs
nprint = min(20, len(eigvar))
print("PC   %Variance   Cumulative%")
for i in range(nprint):
    print(f"{i+1:2d}  {eigvar[i]:8.4f}   {cumulative[i]:8.4f}")



# Save numeric values to file for later
out = "pca_variance.txt"
with open(out, "w") as fh:
    fh.write("PC\t%Variance\tCumulative%\n")
    for i,val,cum in zip(range(1,len(eigvar)+1), eigvar, cumulative):
        fh.write(f"{i}\t{val:.6f}\t{cum:.6f}\n")
print(f"Written {out}")

