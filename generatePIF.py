import numpy as np
from pifpy import pifgen

filename = 'piftest.PIFF'
X = 100
Y = 100
Z = 1

# Layer 1
cell_type = 'Medium'
layer1 = np.zeros((X,Y),dtype=int)
pifgen.write_layer(layer1,cell_type,filename)

# Layer 2
cell_type = 'Cells'
layer2 = np.zeros((X,Y),dtype=int)
cell_width = 10
cell_height = 8
gap = 2
pifgen.populate_layer(layer2,cell_width,cell_height,gap)
pifgen.append_layer(layer2,cell_type,filename)

# Layer 3
cell_type = 'Wall'
layer3 = np.zeros((X,Y),dtype=int)

wall1 = pifgen.wall_id(layer2,1)
wall2 = pifgen.wall_id(layer2,2)
layer3[0:9] = wall1
layer3[91:100] = wall2

pifgen.append_layer(layer3,cell_type,filename)
