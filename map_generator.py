import random

map_height = 15
map_width = 15
new_map = []

# Initial map creation
for y in range(0, map_height):
    new_map.append([])
    for x in range(0, map_width):
        new_map[y].append('#')

# First cell initialisation
new_map[0][0] = '_'
new_map[map_height-1][map_width-1] = 'A'

# Cell propagation function
def cell_propagation(map_name, cell_coordinates):
    cells_around = {
          "top_cell": (cell_coordinates[0]+1, cell_coordinates[1]),
          "left_cell": (cell_coordinates[0], cell_coordinates[1]-1),
          "bottom_cell": (cell_coordinates[0]-1, cell_coordinates[1]),
          "right_cell": (cell_coordinates[0], cell_coordinates[1]+1)
        }

    # Counting cells around
    cells_around_names = []
    for cell in cells_around:
        if cells_around[cell][0] >= 0 and cells_around[cell][0] < len(map_name):
            if cells_around[cell][1] >= 0 and cells_around[cell][1] < len(map_name[0]):
                cells_around_names.append(cell)
                """if map_name[cells_around[cell][0]][cells_around[cell][1]] == '#':
                    if random.random() < 0.5:
                        map_name[cells_around[cell][0]][cells_around[cell][1]] = '_'
                        cell_propagation(map_name, (cells_around[cell][0], cells_around[cell][1]))"""

    # Propagating cells
    if cells_around_names != []:
        random_cell_position = random.randint(0, len(cells_around_names)-1)
        random_cell_around = cells_around_names[random_cell_position]
        if map_name[cells_around[random_cell_around][0]][cells_around[random_cell_around][1]] != 'A':
            map_name[cells_around[random_cell_around][0]][cells_around[random_cell_around][1]] = '_'
            # Map print
            """print("===============")
            for y in range(0, len(new_map)):
                map_line = ''
                for x in range(0, len(new_map[y])):
                    map_line += new_map[y][x]
                print(map_line)"""
            cell_propagation(map_name, (cells_around[random_cell_around][0],cells_around[random_cell_around][1]))
    
        
    
# Calling the function
cell_propagation(new_map, (0, 0))

# Map print
for y in range(0, len(new_map)):
    map_line = ''
    for x in range(0, len(new_map[y])):
        map_line += new_map[y][x]
    print(map_line)
