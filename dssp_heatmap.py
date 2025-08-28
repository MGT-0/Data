import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm

# Load your DSSP data (frames × residues)
data = np.loadtxt('trial21.dssp.dat', dtype=int)

n_frames, n_residues = data.shape

# Define vibrant colors for each DSSP code 0–7
colors = [
    "#1f77b4",  # 0  Coil (blue)
    "#ff7f0e",  # 1  Ext  (orange)
    "#2ca02c",  # 2  Brg  (green)
    "#9467bd",  # 3  3-10 (purple)
    "#d62728",  # 4  α-helix (red)
    "#bcbd22",  # 5  π-helix (olive/yellow)
    "#17becf",  # 6  Turn (cyan)
    "#e377c2",  # 7  Bend (magenta)
]
cmap = ListedColormap(colors)
norm = BoundaryNorm(np.arange(-0.5, 8.5, 1), cmap.N)

plt.figure(figsize=(12, 4))
plt.imshow(
    data.T,
    aspect='auto',
    interpolation='nearest',
    cmap=cmap,
    norm=norm
)

# Colorbar with labels
cbar = plt.colorbar(ticks=np.arange(8), fraction=0.046, pad=0.04)
cbar.set_ticklabels([
    'Coil', 'Ext', 'Brg', '3-10', 'α-helix', 'π-helix', 'Turn', 'Bend'
])

# Axes labels and ticks
plt.xlabel('Frame')
plt.ylabel('Residue Number')
plt.yticks(
    ticks=np.arange(n_residues),
    labels=np.arange(185, 185 + n_residues)
)

plt.title('Secondary‐Structure Timeline (Trial 21)')
plt.tight_layout()
plt.show()

