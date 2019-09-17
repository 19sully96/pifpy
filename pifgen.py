import numpy as np

def write_layer(layer,cell_type,filename):
    f = open(filename,'w')
    width = layer.shape[0]
    height = layer.shape[1]
    for row in np.arange(width):
        for col in np.arange(height):
            cell_id = repr(layer[row][col])
            x = repr(row)
            y = repr(col)
            f.write(cell_id + ' ' + cell_type + ' ' + x + ' ' + x + ' ' + y + ' ' + y + ' 0 0\n')
    f.close()

def append_layer(layer,cell_type,filename):
    f = open(filename,'a')
    width = layer.shape[0]
    height = layer.shape[1]
    for row in np.arange(width):
        for col in np.arange(height):
            if layer[row][col]!=0:
                cell_id = repr(layer[row][col])
                x = repr(row)
                y = repr(col)
                f.write(cell_id + ' ' + cell_type + ' ' + x + ' ' + x + ' ' + y + ' ' + y + ' 0 0\n')
    f.close()

def populate_layer(layer,cell_width,cell_height,gap):
    width = layer.shape[0]
    height = layer.shape[1]
    loop_width = cell_width + gap
    loop_height = cell_height + gap
    x_iterations = np.floor(width/loop_width)
    
    if gap == 0:
        multiplier = 0
    else:
        multiplier = -1
        
    for y in np.arange(height,dtype=int):
        
        if (y)%loop_height < gap:
            layer[y][:] = 0
        
        else:
            for x in np.arange(x_iterations,dtype=int):
                layer[y][x*loop_width:x*loop_width + gap] = 0
                layer[y][x*loop_width + gap:loop_width + x*loop_width ] = (x+1) + multiplier*x_iterations
        
        if y%loop_height == 0:
            multiplier += 1

def new_id(layer,n):
    new_id = layer.max() + n
    return new_id
