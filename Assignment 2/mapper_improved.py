# from mapper import *
import random
from map import *

def enum(**enums):
    return type('Enum', (), enums)

DIRECTION = enum(North=1, East=2, South=3, West=4)

def checkSensors():
    # set the threshold values for the sensors 
    thresh_left_high = 800
    thresh_left_low = 290

    thresh_right_high = 800
    thresh_right_low = 290

    thresh_front_high = 2200
    thresh_front_low = 1900

    front_sensor_val = getSensorValue(3) # check later
    right_sensor_val = getSensorValue(4) # check sensor ID
    left_sensor_val = getSensorValue(2) # check sensor ID

    sensorsBlocked = []

    if (left_sensor_val >= thresh_left_low) and (left_sensor_val <= thresh_left_high):
        sensorsBlocked.append(True)
    else:
        sensorsBlocked.append(False)

    if (right_sensor_val >= thresh_right_low) and (right_sensor_val <= thresh_right_high):
        sensorsBlocked.append(True)
    else:
        sensorsBlocked.append(False)
    
    if (front_sensor_val >= thresh_front_low) and (front_sensor_val <= thresh_front_high):
        sensorsBlocked.append(True)
    else:
        sensorsBlocked.append(False)

    return sensorsBlocked # order is [Left Sensor, Right Sensor, Front Sensor]

def turn2NewPos(turn_command,current_position):
    # key point: all turns are made in reference to a global coordinate system set at the top left of the map 
    # & facing south
    i_curr = current_position[0]
    j_curr = current_position[1]
    k_curr = current_position[2] # position kept as absolute

    dir = k_curr

    if turn_command == "Forward":
        # forward does not change the heading
        if dir == DIRECTION.South:
            i_new = i_curr + 1
            j_new = j_curr
            k_new = k_curr
            dir_new = k_new

        elif dir == DIRECTION.North:
            i_new = i_curr - 1
            j_new = j_curr
            k_new = k_curr
            dir_new = k_new

        elif dir == DIRECTION.East:
            i_new = i_curr
            j_new = j_curr + 1
            k_new = k_curr
            dir_new = k_new

        elif dir == DIRECTION.West:
            i_new = i_curr
            j_new = j_curr - 1
            k_new = k_curr
            dir_new = k_new
        else:
            print("Error ID 1: Please input proper direction.")

    elif turn_command == "Left":
        if dir == DIRECTION.South:
            # new heading = East
            i_new = i_curr
            # j_new = j_curr + 1
            j_new = j_curr
            k_new = DIRECTION.East
            dir_new = k_new

        elif dir == DIRECTION.North:
            # new heading = West
            i_new = i_curr
            # j_new = j_curr - 1
            j_new = j_curr 
            k_new = DIRECTION.West
            dir_new = k_new

        elif dir == DIRECTION.East:
            # new heading = North
            # i_new = i_curr - 1 
            i_new = i_curr
            j_new = j_curr 
            k_new = DIRECTION.North
            dir_new = k_new

        elif dir == DIRECTION.West:
            # new heading = South
            # i_new = i_curr + 1
            i_new = i_curr
            j_new = j_curr
            k_new = DIRECTION.South
            dir_new = k_new
        else:
            print("Error ID 2: Please input proper direction.")
    
    elif turn_command == "Right":
        if dir == DIRECTION.South:
            # new heading = West
            # i_new = i_curr
            i_new = i_curr
            # j_new = j_curr - 1
            j_new = j_curr
            k_new = DIRECTION.West
            dir_new = k_new

        elif dir == DIRECTION.North:
            # new heading = East
            i_new = i_curr
            # j_new = j_curr + 1
            j_new = j_curr
            k_new = DIRECTION.East
            dir_new = k_new

        elif dir == DIRECTION.East:
            # new heading = South
            # i_new = i_curr + 1
            i_new = i_curr
            j_new = j_curr 
            k_new = DIRECTION.South
            dir_new = k_new

        elif dir == DIRECTION.West:
            # new heading = North
            # i_new = i_curr - 1
            i_new = i_curr
            j_new = j_curr
            k_new = DIRECTION.North
            dir_new = k_new
        else:
            print("Error ID 3: Please input proper direction.")

    elif turn_command == "Turn Around":
        # turn around should only change orientation
        if dir == DIRECTION.South:
            # new heading = North
            i_new = i_curr
            j_new = j_curr
            k_new = DIRECTION.North
            dir_new = k_new

        elif dir == DIRECTION.North:
            # new heading = South
            i_new = i_curr
            j_new = j_curr
            k_new = DIRECTION.South
            dir_new = k_new

        elif dir == DIRECTION.East:
            # new heading = West
            i_new = i_curr
            j_new = j_curr 
            k_new = DIRECTION.West
            dir_new = k_new

        elif dir == DIRECTION.West:
            # new heading = East
            i_new = i_curr
            j_new = j_curr
            k_new = DIRECTION.East
            dir_new = k_new
        else:
            print("Error ID 4: Please input proper direction.")
    else:
        print("Error ID 0: Please enter proper turn command.")
    
    return (i_new,j_new,k_new)

def decideNextMove(all_moves,current_pos,sensorsBlocked,moves_list):
    possible_headings = ["North","South","East","West"] # a set

    if len(all_moves) == 0: # start position
        all_moves.update({(0,0):[3]}) # seed the start position

    # first check if the current position has been visited already:
    all_positions = all_moves.keys() # get all the positions
    print("all moves: ", all_moves)
    print("all positions: ", all_positions)

    # get just the i & j values of the robot's location
    pos_only = (current_pos[0],current_pos[1])

    # if (sensorsBlocked[0] is False) and (sensorsBlocked[1] is False) and (sensorsBlocked[2] is False):
    #     # no sensors blocked, all movements possible
    #     possible_turn_commands = ["Forward","Left","Right"]


    if pos_only in all_positions: # if the cell has been visited before
        completed_headings = all_moves[pos_only] # get a list of headings at the current position

        suggested_pos_list = []
        suggested_headings = []
        # sensorsBlocked = checkSensors()
        if (sensorsBlocked[0] is True) and (sensorsBlocked[1] is True) and (sensorsBlocked[2] is True):
            turn_command = "Turn Around"
            suggested_headings.append(turn2NewPos(turn_command,current_pos)[2])
            suggested_pos_list.append(turn2NewPos(turn_command,current_pos))

        elif (sensorsBlocked[0] is True) and (sensorsBlocked[1] is True) and (sensorsBlocked[2] is False):
        # left & right sensors are blocked but front sensor is not
            turn_command = "Forward"
            suggested_headings.append(turn2NewPos(turn_command,current_pos)[2])
            suggested_pos_list.append(turn2NewPos(turn_command,current_pos))

        elif (sensorsBlocked[0] is True) and (sensorsBlocked[1] is False) and (sensorsBlocked[2] is True):
        # left & front sensors blocked while right sensor not
            turn_command = "Right"
            suggested_headings.append(turn2NewPos(turn_command,current_pos)[2])
            suggested_pos_list.append(turn2NewPos(turn_command,current_pos))

        elif (sensorsBlocked[0] is False) and (sensorsBlocked[1] and True) and (sensorsBlocked[2] is True):
            # right & front sensors blocked
            turn_command = "Left"
            suggested_headings.append(turn2NewPos(turn_command,current_pos)[2])
            suggested_pos_list.append(turn2NewPos(turn_command,current_pos))
        
        elif (sensorsBlocked[0] is True) and (sensorsBlocked[1] is False) and (sensorsBlocked[2] is False):
            # only left sensor blocked -> can go forward OR right
            possible_turn_commands = ["Forward","Right"]
            # print("Turn command is: ", turn_command)
            for command in possible_turn_commands:
                suggested_headings.append(turn2NewPos(command,current_pos)[2])
                suggested_pos_list.append(turn2NewPos(command,current_pos))

        elif (sensorsBlocked[0] is False) and (sensorsBlocked[1] is True) and (sensorsBlocked[2] is False):
            # only right sensor blocked -> can go forward OR left
            possible_turn_commands = ["Left","Forward"]
            for command in possible_turn_commands:
                suggested_headings.append(turn2NewPos(command,current_pos)[2])
                suggested_pos_list.append(turn2NewPos(command,current_pos))
            
        elif (sensorsBlocked[0] is False) and (sensorsBlocked[1] is False) and (sensorsBlocked[2] is True):
            # only front sensor blocked -> can go left OR right
            possible_turn_commands = ["Left","Right"]
            for command in possible_turn_commands:
                suggested_headings.append(turn2NewPos(command,current_pos)[2])
                suggested_pos_list.append(turn2NewPos(command,current_pos))
        
        else:
            # if no sensors blocked but cell visited before,
            # choose a random heading based on headings not yet visited
            # COME BACK TO THIS!
            possible_turn_commands = ["Forward","Left","Right"]
            for command in possible_turn_commands:
                suggested_headings.append(turn2NewPos(command,current_pos)[2])
                suggested_pos_list.append(turn2NewPos(command,current_pos))
        
        # so now have a list of suggested headings based on the sensor data
        # loop through the headings to figure out if any have not been completed yet

        print("suggested headings: ", suggested_headings)
        print("suggested positions ", suggested_pos_list)

        # iterate through all suggested next moves
        for ii in range(len(suggested_headings)):
            head = suggested_headings[ii] # a particular next move
            if head in completed_headings: # if this move has been completed
                if head == current_pos[2]: # but if the heading is in the same direction as before
                    next_pos = suggested_pos_list[ii]
                    next_heading = suggested_headings[ii] # keep going forward

                # next_pos = suggested_pos_list[ii]
                # next_heading = suggested_headings[ii]
                else:
                    # check how many times it came to that exact position
                    times_visited = moves_list.count(suggested_pos_list[ii])

                    if times_visited < 3: # if it hasn't visited the cell too many times
                        next_pos = suggested_pos_list[ii]
                        next_heading = suggested_headings[ii]

                    else: # visited this cell several times in this direction
                        next_pos = current_pos
                        next_heading = current_pos[2] # keep this here in case all headings completed
                        continue # check next head
            else:
                next_pos = suggested_pos_list[ii]
                next_heading = suggested_headings[ii]
                break # if one found, do not re-enter the loop

    else: # robot arrived at a new cell, use sensors to determine next move
        print("Arrived at new cell!")
        if (sensorsBlocked[0] is True) and (sensorsBlocked[1] is True) and (sensorsBlocked[2] is True):
            # if all sensors are blocked
            turn_command = "Turn Around"
            next_pos = turn2NewPos(turn_command,current_pos)
            # next_pos_only = (next_pos[0],next_pos[1])
            next_heading = turn2NewPos(turn_command,current_pos)[2]

        elif (sensorsBlocked[0] is True) and (sensorsBlocked[1] is True) and (sensorsBlocked[2] is False):
            # left & right sensors are blocked but front sensor is not
            turn_command = "Forward"
            next_pos = turn2NewPos(turn_command,current_pos)
            next_heading = turn2NewPos(turn_command,current_pos)[2]
            
        elif (sensorsBlocked[0] is True) and (sensorsBlocked[1] is False) and (sensorsBlocked[2] is True):
            # left & front sensors blocked while right sensor not
            turn_command = "Right"
            next_pos = turn2NewPos(turn_command,current_pos)
            next_heading = turn2NewPos(turn_command,current_pos)[2]

        elif (sensorsBlocked[0] is False) and (sensorsBlocked[1] and True) and (sensorsBlocked[2] is True):
            # right & front sensors blocked
            turn_command = "Left"
            next_pos = turn2NewPos(turn_command,current_pos)
            next_heading = turn2NewPos(turn_command,current_pos)[2]
        
        elif (sensorsBlocked[0] is True) and (sensorsBlocked[1] is False) and (sensorsBlocked[2] is False):
            # only left sensor blocked -> can go forward OR right
            possible_turn_commands = ["Forward","Right"]
            turn_command = possible_turn_commands.pop(0)
            # print("Turn command is: ", turn_command)
            next_pos = turn2NewPos(turn_command,current_pos)
            next_heading = turn2NewPos(turn_command,current_pos)[2]

        elif (sensorsBlocked[0] is False) and (sensorsBlocked[1] is True) and (sensorsBlocked[2] is False):
            # only right sensor blocked -> can go forward OR left
            possible_turn_commands = ["Left","Forward"]
            turn_command = possible_turn_commands.pop(0)
            next_pos = turn2NewPos(turn_command,current_pos)
            next_heading = turn2NewPos(turn_command,current_pos)[2]
            
        elif (sensorsBlocked[0] is False) and (sensorsBlocked[1] is False) and (sensorsBlocked[2] is True):
            # only front sensor blocked -> can go left OR right
            possible_turn_commands = ["Left","Right"]
            turn_command = possible_turn_commands.pop(0) # take the first element
            next_pos = turn2NewPos(turn_command,current_pos)
            next_heading = turn2NewPos(turn_command,current_pos)[2]

        # update all moves with the new move & make a return  
        else:
            # no sensors blocked, choose a direction randomly if new cell
            # but prevent from going back where it came
            possible_turn_commands = ["Forward","Left","Right"]
            turn_command = random.choice(possible_turn_commands)
            next_pos = turn2NewPos(turn_command,current_pos)
            next_heading = turn2NewPos(turn_command,current_pos)[2]
        
    moves_list.append(next_pos)
    return next_pos

# based on information on the past state and next state, move the robot
def moveRobot(current_pos,next_pos,robot_not_moved):
    # compare values of i,j,k in both states, if they are the same, robot should not move:
    if next_pos == current_pos:
        print("don't move")
        robot_not_moved += 1 # increment robot not moved
        pass # don't move robot
    else:
        i_past = current_pos[0]
        j_past = current_pos[1]
        k_past = current_pos[2]

        i_next = next_pos[0]
        j_next = next_pos[1]
        k_next = next_pos[2]

        if (k_past == k_next): # orientation of the robot has not changed
            if (i_past != i_next) or (j_past != j_next):
                # if either the i or j position changed
                print("go forward")
            else:
                print("don't move")
                robot_not_moved += 1
        else:
            if ((k_past == DIRECTION.North) and (k_next == DIRECTION.South)) or \
            ((k_past == DIRECTION.South) and (k_next == DIRECTION.North)) or \
            ((k_past == DIRECTION.East) and (k_next == DIRECTION.West)) or \
            ((k_past == DIRECTION.West) and (k_next == DIRECTION.East)):
            # a 180 degree turn is desired
            # turnAround()
                print("Turn around")

            else:
                # a 90 degree turn is desired
                orientation_diff = k_next - k_past
                if (k_past == DIRECTION.North) or (k_next == DIRECTION.North):
                    if orientation_diff == 3:
                        # the turn occurs from North to West i.e. a left turn
                        # leftTurn() # uncomment later
                        print("left turn")
                        # singleCell()
                    elif (orientation_diff > 0) and (orientation_diff < 3):
                        print("right turn")

                    elif (orientation_diff > -3) and (orientation_diff < 0):
                        print("left turn")

                    elif (orientation_diff == -3):
                        # the turn occurs from West to North, i.e. a right turn
                        # rightTurn() # uncomment later
                        print("right turn")
                        # singleCell()
                    else:
                        print('Error in moveRobot: Unknown or illegal combination of turns')
                
                else:
                    if orientation_diff < 0:
                        # turn occured in the anticlockwise direction i.e. left turn
                        # leftTurn() # uncomment later
                        print("left turn")
                        # singleCell()
                    else:
                        # turn occured in the clockwise direction i.e. right turn
                        print("right turn")
                        # rightTurn() # uncomment later
                        # singleCell()

    return robot_not_moved

# updates map information at current position by tracking sensor information   
def updateMap(obstacle_map, sensorsBlocked, current_position):
    # key point (i think): if a sensor is NOT blocked, does not necessarily mean that there isn't a wall
    # there, robot may just not be close enough to sense the wall. only update blocked walls   

    # extract relevant information
    i = current_position[0]
    j = current_position[1]
    dir = current_position[2]
    
    lsensor_blocked = sensorsBlocked[0]
    rsensor_blocked = sensorsBlocked[1]
    fsensor_blocked = sensorsBlocked[2]

    # update the maps depending on the heading of the robot & which sensors are blocked

    # if robot is heading south
    if dir == DIRECTION.South:
        if lsensor_blocked is True:
            obstacle_dir = DIRECTION.East
            isBlocked = 1
            # print("Facing South: left wall blocked")
            # obstacle_map.setObstacle(i,j,isBlocked,obstacle_dir)

        if rsensor_blocked is True:
            obstacle_dir = DIRECTION.West
            isBlocked = 1
            # print("Facing South: right wall blocked")
            # obstacle_map.setObstacle(i,j,isBlocked,obstacle_dir)
        
        if fsensor_blocked is True:
            obstacle_dir = DIRECTION.South
            isBlocked = 1
            # print("Facing South: front wall blocked")
            # obstacle_map.setObstacle(i,j,isBlocked,obstacle_dir)

    # if robot is heading north
    elif dir == DIRECTION.North:
        if lsensor_blocked is True:
            obstacle_dir = DIRECTION.West
            isBlocked = 1
            # obstacle_map.setObstacle(i,j,isBlocked,obstacle_dir)
            # print("Facing North: left wall blocked")

        if rsensor_blocked is True:
            obstacle_dir = DIRECTION.East
            isBlocked = 1
            # obstacle_map.setObstacle(i,j,isBlocked,obstacle_dir)
            # print("Facing North: right wall blocked")
        
        if fsensor_blocked is True:
            obstacle_dir = DIRECTION.North
            isBlocked = 1
            # obstacle_map.setObstacle(i,j,isBlocked,obstacle_dir)
            # print("Facing North: front wall blocked")
    
    # if robot is heading east
    elif dir == DIRECTION.East:
        if lsensor_blocked is True:
            obstacle_dir = DIRECTION.North
            isBlocked = 1
            # obstacle_map.setObstacle(i,j,isBlocked,obstacle_dir)
            # print("Facing East: left wall blocked")


        if rsensor_blocked is True:
            obstacle_dir = DIRECTION.South
            isBlocked = 1
            # obstacle_map.setObstacle(i,j,isBlocked,obstacle_dir)
            # print("Facing East: right wall blocked")
        
        if fsensor_blocked is True:
            obstacle_dir = DIRECTION.East
            isBlocked = 1
            # obstacle_map.setObstacle(i,j,isBlocked,obstacle_dir)
            # print("Facing East: front wall blocked")

    # if robot is heading west
    elif dir == DIRECTION.West:
        if lsensor_blocked is True:
            obstacle_dir = DIRECTION.South
            isBlocked = 1
            # obstacle_map.setObstacle(i,j,isBlocked,obstacle_dir)
            # print("Facing West: left wall blocked")

        if rsensor_blocked is True:
            obstacle_dir = DIRECTION.North
            isBlocked = 1
            # obstacle_map.setObstacle(i,j,isBlocked,obstacle_dir)
            # print("Facing West: right wall blocked")

        if fsensor_blocked is True:
            obstacle_dir = DIRECTION.West
            isBlocked = 1
            # obstacle_map.setObstacle(i,j,isBlocked,obstacle_dir)
            # print("Facing West: front wall blocked")
    
    else:
        print('Error in updateMaps: Unknown value of DIRECTION entered.')

### TEST CODE: ###
# sensorsBlocked = [[True,True,False],[True,True,False],[False,True,True],
#                 [True,True,False],[True,True,False],[True,False,True],
#                 [True,True,False],[True,True,True],[True,True,False],
#                 [False,True,True],[True,True,False],[False,False,False],
#                 [True,True,False],[False,False,False],[True,True,False],
#                 [False,True,False],[True,True,False]]

# sensorsBlocked = [[True,True,False] for x in range(10)]
                  
all_moves = {}
moves_list = []
pos = (0,0,3)
obstacle_map = []
sensorsBlocked = checkSensors()
# for combination in sensorsBlocked:
robot_not_moved = 0 # initialize counter
while robot_not_moved < 4: # while the robot hasn't been stationary for more than 4 iterations
    updateMap(obstacle_map,sensorsBlocked,pos)
    next_pos = decideNextMove(all_moves,pos,sensorsBlocked,moves_list)
    print("next pos: ", next_pos)
    print("moves list: ", moves_list)
    robot_not_moved = moveRobot(pos,next_pos)

    next_pos_only = (next_pos[0],next_pos[1])
    next_heading = next_pos[2]
    if next_pos_only in all_moves.keys():
        if next_heading not in all_moves[next_pos_only]:
            all_moves[next_pos_only].append(next_heading)
    else:
        all_moves.update({next_pos_only:[next_heading]})

    pos = next_pos.copy()

unique_cells = len(all_moves.keys())
print("The robot arrived at ", unique_cells, " unique cells.")

