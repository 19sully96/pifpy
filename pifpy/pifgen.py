import numpy as np

def write_layer(layer,cell_type,filename):
    f = open(filename,'w')
    width = layer.shape[0]
    height = layer.shape[1]
    for row in np.arange(width):
        for col in np.arange(height):
            cell_id = repr(layer[row][col])
            x = repr(col)
            y = repr(row)
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
                x = repr(col)
                y = repr(row)
                f.write(cell_id + ' ' + cell_type + ' ' + x + ' ' + x + ' ' + y + ' ' + y + ' 0 0\n')
    f.close()

def populate_uniform(layer,cell_width,cell_height,gap):
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
            
def populate_random(layer, n_cells, start_id):
    x_max = np.shape(layer)[1]
    y_max = np.shape(layer)[0]
    rand_xcoord = np.random.randint(0,x_max,n_cells)
    rand_ycoord = np.random.randint(0,y_max,n_cells)
    for i in np.arange(n_cells):
        if layer[rand_ycoord[i]][rand_xcoord[i]] != 0:
            new_x = np.random.randint(0,x_max)
            new_y = np.random.randint(0,y_max)
            while layer[new_y][new_x] != 0:
                new_x = np.random.randint(0,x_max)
                new_y = np.random.randint(0,y_max)
            layer[new_y][new_x] = start_id + i
        else:
            layer[rand_ycoord[i]][rand_xcoord[i]] = start_id + i         
            
def get_id(layer,n):
    get_id = layer.max() + n
    return get_id

def square_cell(layer,cell_id,cell_width,cell_height,x,y): 
    # x and y are center coordinates of cell 
    dx = np.int(cell_width/2)
    dy = np.int(cell_height/2)
    layer[y-dy:y+dy,x-dx:x+dx] = cell_id
    return layer
