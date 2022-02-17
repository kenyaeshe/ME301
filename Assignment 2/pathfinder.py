from map import *
# recall i is North-South, j is East-West
# Usage:
#
# #Create object
# your_map = EECSMap()
#
# #Use Object (examples)
# your_map.printObstacleMap()
# your_map.clearObstacleMap()
# your_map.printCostMap()
# your_map.setObstacle(3, 4, 1, DIRECTION.North)
# isBlocked = your_map.getObstacle(3, 4, DIRECTION.North)
# cell_cost = your_map.getCost(3, 4)

# pathfinding method: waveform propagation

# generate the map
gridmap = EECSMap()
gridmap.printCostMap()
gridmap.printObstacleMap()
# print(gridmap)

# define start & goal position
goal_cell = (1,1)
start_cell = (5,6)

# initialize lists & variables
open_cells = [] # cells which are actively being used
closed_cells = [] # cells for which all neighbors have been assigned cost or is an obstacle
blocked_cells = []
goalFound = 0
highest_cost = 0
open_cells.append(goal_cell)

# define the positions
directions = [DIRECTION.North,DIRECTION.South, DIRECTION.East,DIRECTION.West]

# initialize the cost
cost = 2

# initialize the cost of the goal cell
gridmap.setCost(goal_cell[0],goal_cell[1],cost)

while not goalFound:
    if len(open_cells) == 0:
        print("could not find a path :(")
        break # need to figure out how to ensure a path is found

    # take the first element in the open list & check its neighbours
    closed_cells.append(open_cells[0])
    
    current_cell = open_cells.pop(0)
    print("current cell: ", current_cell)
    i_val = current_cell[0]
    j_val = current_cell[1]
    current_cost = gridmap.getCost(i_val,j_val)
    print("Current cost is: ", current_cost)

    if current_cost > highest_cost:
        highest_cost = current_cost
    
    for dir in directions:
        
        # define the possible neighbor locations
        if dir == DIRECTION.North:
            neighbor_i_val = i_val + 1
            neighbor_j_val = j_val
        elif dir == DIRECTION.South:
            neighbor_i_val = i_val - 1
            neighbor_j_val = j_val
        elif dir == DIRECTION.East:
            neighbor_i_val = i_val
            neighbor_j_val = j_val + 1
        else: # else the direction is west
            neighbor_i_val = i_val
            neighbor_j_val = j_val - 1
        
        neighbor_location = (neighbor_i_val,neighbor_j_val)
        print("checking neighbor: ", neighbor_location)

        # check if neighbor out of bounds:
        if (neighbor_i_val >= 8) or (neighbor_i_val < 0) or (neighbor_j_val >= 8) or (neighbor_j_val < 0):
            print("neighbor out of bounds")
            continue # neighbor out of range, check next neighbor

        # check if neighbor is the startPos
        elif (neighbor_i_val == start_cell[0]) and (neighbor_j_val == start_cell[1]):
            """ if the i & j value of the neighbor matches the i & j of the start cell,
             the goal is found
             update the cost of the start cell to ensure the path can be retraced """

            print("Goal found!")
            
            # new_cost = current_cost + 10 # set a higher number to differentiate the goal
            new_cost = highest_cost + 3
            
            # gridmap.setNeighborCost(i_val,j_val,dir,new_cost)
            # gridmap.setNeighborCost(neighbor_i_val,neighbor_j_val,dir,new_cost)
            gridmap.setCost(neighbor_i_val,neighbor_j_val,new_cost)
            goalFound = 1
            break 

        elif neighbor_location in closed_cells: # check if neighbor already in closed cell list
            print("Neighbor already checked")
            continue # check the next neighbor

        else: # check if neighbor is blocked or accessible
            neighbor_blocked = gridmap.getNeighborObstacle(neighbor_i_val,neighbor_j_val,dir) # returns isBlocked
            # print('neighbor blocked val: ',neighbor_blocked)
            # if the neighbor is an obstacle, add to closed list
            if neighbor_blocked == 1:
                print("Neighbor blocked :(")
                # gridmap.setCost(neighbor_i_val,neighbor_j_val,current_cost-2)
                # gridmap.setCost(neighbor_i_val,neighbor_j_val,1)
                # closed_cells.append(neighbor_location)
                # open_cells.append(neighbor_location)
                continue
            else:
                print("Neighbor open :)")
                open_cells.append(neighbor_location)
                new_cost = current_cost + 1
                # gridmap.setNeighborCost(i_val,j_val,dir,new_cost)
                gridmap.setCost(neighbor_i_val,neighbor_j_val,new_cost)
            
# print the new map
# print("Open cells: ", open_cells)
# print("Closed cells: ", closed_cells)
gridmap.printCostMap()
    
# find a path from goal to start




