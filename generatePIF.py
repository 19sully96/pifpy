# Generic format of generatePIF.py file
#
# This file should be copied to one directory above location of pifpy.  If placed in a different location, 
# you will need to add pifpy to your python path. 

import numpy as np
from pifpy import pifgen

# General PIF information
filename = 'filename.PIF'
X = 256  # dimensions in pixels
Y = 256
Z = 1    # Current pifgen functions only allow 2D configurations

# Layer 1
cell_type = 'Medium'
layer1 = np.zeros((X,Y),dtype=int)
pifgen.write_layer(layer1,cell_type,filename)

# Layer 2
cell_type = 'Cells'
layer2 = np.zeros((X,Y),dtype=int)
cell_width = 10
cell_height = 10
gap = 5
pifgen.populate_layer(layer2,cell_width,cell_height,gap)
pifgen.append_layer(layer2,cell_type,filename)

# Layer 3
cell_type = 'Wall'
layer3 = np.zeros((X,Y),dtype=int)

wall_width = 10
wall1 = pifgen.get_id(layer2,1)
wall2 = pifgen.get_id(layer2,2)
layer3[:,0:wall_width-1] = wall1    # left wall
layer3[:,X-wallwidth:X-1] = wall2    # right wall

pifgen.append_layer(layer3,cell_type,filename)
