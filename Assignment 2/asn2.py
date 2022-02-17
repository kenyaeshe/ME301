#!/usr/bin/env python
# from tracemalloc import start
from os import times
import roslib
import rospy
import time
import random
from map import *
# from mapper_improved import *

from fw_wrapper.srv import *

# GROUP A: Kenya Alexander + Alex Cindric
# Assignment 1 - Control: Feedback & Reactive

# -----------SERVICE DEFINITION-----------
# allcmd REQUEST DATA
# ---------
# string command_type
# int8 device_id
# int16 target_val
# int8 n_dev
# int8[] dev_ids
# int16[] target_vals

# allcmd RESPONSE DATA
# ---------
# int16 val
# --------END SERVICE DEFINITION----------

# ----------COMMAND TYPE LIST-------------
# GetMotorTargetPosition
# GetMotorCurrentPosition
# GetIsMotorMoving
# GetSensorValue
# GetMotorWheelSpeed
# SetMotorTargetPosition
# SetMotorTargetSpeed
# SetMotorTargetPositionsSync
# SetMotorMode
# SetMotorWheelSpeed

# wrapper function to call service to set a motor mode
# 0 = set target positions, 1 = set wheel moving
def setMotorMode(motor_id, target_val):
    rospy.wait_for_service('allcmd')
    try:
        send_command = rospy.ServiceProxy('allcmd', allcmd)
        resp1 = send_command('SetMotorMode', motor_id, target_val, 0, [0], [0])
        return resp1.val
    except rospy.ServiceException,e:
        print("Service call failed: %s"%e)

# wrapper function to call service to get motor wheel speed
def getMotorWheelSpeed(motor_id):
    rospy.wait_for_service('allcmd')
    try:
        send_command = rospy.ServiceProxy('allcmd', allcmd)
        resp1 = send_command('GetMotorWheelSpeed', motor_id, 0, 0, [0], [0])
        return resp1.val
    except rospy.ServiceException,e:
        print("Service call failed: %s")%e

# wrapper function to call service to set motor wheel speed
def setMotorWheelSpeed(motor_id, target_val):
    rospy.wait_for_service('allcmd')
    try:
        send_command = rospy.ServiceProxy('allcmd', allcmd)
        resp1 = send_command('SetMotorWheelSpeed', motor_id, target_val, 0, [0], [0])
        return resp1.val
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

# wrapper function to call service to set motor target speed
def setMotorTargetSpeed(motor_id, target_val):
    rospy.wait_for_service('allcmd')
    try:
        send_command = rospy.ServiceProxy('allcmd', allcmd)
        resp1 = send_command('SetMotorTargetSpeed', motor_id, target_val, 0, [0], [0])
        return resp1.val
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

# wrapper function to call service to get sensor value
def getSensorValue(port):
    rospy.wait_for_service('allcmd')
    try:
        send_command = rospy.ServiceProxy('allcmd', allcmd)
        resp1 = send_command('GetSensorValue', port, 0, 0, [0], [0])
        return resp1.val
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

# wrapper function to call service to set a motor target position
# need to check that this was properly altered:
def setMotorTargetPositionCommand(motor_id, target_val):
    rospy.wait_for_service('allcmd')
    try:
        send_command = rospy.ServiceProxy('allcmd', allcmd)
        resp1 = send_command('SetMotorTargetPosition', motor_id, target_val, 0, [0], [0])
        return resp1.val
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

# def setMotorTargetPositionsSync(n_dev,dev_ids, target_vals):

#     rospy.wait_for_service('allcmd')
#     try:
#         send_command = rospy.ServiceProxy('allcmd', allcmd)
#         # resp1 = send_command('SetMotorTargetPositionsSync', n_dev, dev_ids, target_vals, 0, [0], [0])
#         resp1 = send_command('SetMotorTargetPositionsSync', [0], [0], n_dev, dev_ids, target_vals)
#         # req.n_dev, req.dev_ids[0], req.target_vals[0], req.dev_ids[1], req.target_vals[1])
#         return resp1.val
#     except rospy.ServiceException, e:
#         print "Service call failed: %s"%e

# wrapper function to call service to get a motor's current position
def getMotorPositionCommand(motor_id):
    rospy.wait_for_service('allcmd')
    try:
        send_command = rospy.ServiceProxy('allcmd', allcmd)
        resp1 = send_command('GetMotorCurrentPosition', motor_id, 0, 0, [0], [0])
        return resp1.val
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

# wrapper function to call service to check if a motor is currently moving
def getIsMotorMovingCommand(motor_id):
    rospy.wait_for_service('allcmd')
    try:
        send_command = rospy.ServiceProxy('allcmd', allcmd)
        resp1 = send_command('GetIsMotorMoving', motor_id, 0, 0, [0], [0])
        return resp1.val
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e

# FORWARD GAIT FUNCTIONS
motor1 = 1
motor2 = 2
motor3 = 3
motor4 = 4
motor5 = 5
motor6 = 6
motor7 = 7
motor8 = 8
dirs = [1, 2, 3, 4]

def singleCell():
    setMotorMode(motor1,1)
    setMotorMode(motor2,1)
    setMotorMode(motor3,1)
    setMotorMode(motor4,1)
    end_time = time.time() + 2.4 # 5 seconds later

    while time.time() < end_time:
        setMotorWheelSpeed(motor1, 800)
        setMotorWheelSpeed(motor2, 800+1024)
        setMotorWheelSpeed(motor3, 800)
        setMotorWheelSpeed(motor4, 800+1024)
    setMotorWheelSpeed(motor1, 0)
    setMotorWheelSpeed(motor2, 0)
    setMotorWheelSpeed(motor3, 0)
    setMotorWheelSpeed(motor4, 0)


def rightTurn():
    setMotorMode(motor1,1)
    setMotorMode(motor2,1)
    setMotorMode(motor3,1)
    setMotorMode(motor4,1)
    
    end_time = time.time() + 2.9 # 5 seconds later

    while time.time() < end_time:
        setMotorWheelSpeed(motor1, 300)
        setMotorWheelSpeed(motor2, 300)
        setMotorWheelSpeed(motor3, 300)
        setMotorWheelSpeed(motor4, 300)
    setMotorWheelSpeed(motor1, 0)
    setMotorWheelSpeed(motor2, 0)
    setMotorWheelSpeed(motor3, 0)
    setMotorWheelSpeed(motor4, 0)

def leftTurn():
    setMotorMode(motor1,1)
    setMotorMode(motor2,1)
    setMotorMode(motor3,1)
    setMotorMode(motor4,1)
    end_time = time.time() + 3.1 # 5 seconds later

    while time.time() < end_time:
        setMotorWheelSpeed(motor1, 300+1024)
        setMotorWheelSpeed(motor2, 300+1024)
        setMotorWheelSpeed(motor3, 300+1024)
        setMotorWheelSpeed(motor4, 300+1024)
    setMotorWheelSpeed(motor1, 0)
    setMotorWheelSpeed(motor2, 0)
    setMotorWheelSpeed(motor3, 0)
    setMotorWheelSpeed(motor4, 0)

def turnAround():
    setMotorMode(motor1,1)
    setMotorMode(motor2,1)
    setMotorMode(motor3,1)
    setMotorMode(motor4,1)
    end_time = time.time() + 6 # 5 seconds later

    while time.time() < end_time:
        setMotorWheelSpeed(motor1, 300)
        setMotorWheelSpeed(motor2, 300)
        setMotorWheelSpeed(motor3, 300)
        setMotorWheelSpeed(motor4, 300)
    setMotorWheelSpeed(motor1, 0)
    setMotorWheelSpeed(motor2, 0)
    setMotorWheelSpeed(motor3, 0)
    setMotorWheelSpeed(motor4, 0)

def simpleNav(y, x, theta):
    end_time = time.time() + 10 # 5 seconds later

    while time.time() < end_time:
        pass
    origin = [0, 0, 0]
    y_del = y - origin[0]
    x_del = x - origin[1]
    theta_del = theta - origin[0]
    if y_del < 0:
        turnAround()
    else:
        pass
    for i in range(abs(y_del)):
        singleCell()
        print("one i cell")
    if x_del > 0:
        leftTurn()
    if x_del < 0: 
        rightTurn()
    else:
        pass
    for i in range(abs(x_del)):
        singleCell()
        print("one j cell")
    #need to add logic for theta using below definitions 
    #south = = 0
    #north = = 180
    #east = = 90
    #west = = 270
    #dirCorrect = theta_del/90
    

def simpleNavCorrective(y, x, theta):
    origin = [0, 0, 0]
    y_del = y - origin[0]
    x_del = x - origin[1]
    theta_del = theta - origin[0]
    if y_del < 0:
        turnAround()
    else:
        pass
    for i in range(abs(y_del)):
        singleCell()
        print("one i cell")
    if x_del > 0:
        leftTurn()
    if x_del < 0: 
        rightTurn()
    else:
        pass
    for i in range(abs(x_del)):
        singleCell()
        print("one j cell")
    #need to add logic for theta using below definitions 
    #south = = 0
    #north = = 180
    #east = = 90
    #west = = 270
    dirCorrect = theta_del/90

def forwardWheel():
    end_time = time.time() + 5 # 5 seconds later

    while time.time() < end_time:
        setMotorWheelSpeed(motor1, 300)
        setMotorWheelSpeed(motor2, 300+1024)
        setMotorWheelSpeed(motor3, 300)
        setMotorWheelSpeed(motor4, 300+1024)
    setMotorWheelSpeed(motor1, 0)
    setMotorWheelSpeed(motor2, 0)
    setMotorWheelSpeed(motor3, 0)
    setMotorWheelSpeed(motor4, 0)

def deadCells(xs, xg):
    skipCells = []

    mapSize = [8,8]
    numDirs = 4
    deadCost = 1023

    #immediately rule out all initial dead end cells 
    count = 0
    for i in range(mapSize[0]):
        for j in range(mapSize[1]):
            dirBlock = [0, 0, 0, 0]
            sumBlock = 0
            neighborLoc = [i, j]
            for k in range(numDirs):
                dirStat = gridmap.getNeighborObstacle(i, j, k)
                dirBlock[k] = dirStat
            for s in range(len(dirBlock)):
                if dirBlock[s] != 0:
                    sumBlock = sumBlock + 1
            if sumBlock >= 3:
                if i == xs[0] and j == xs[1]:
                    pass
                elif i == xg[0] and j == xg[1]:
                    pass
                else: 
                    skipCells.append(neighborLoc)
                    count = count+1
                    gridmap.setCost(neighborLoc[0], neighborLoc[1], deadCost)
    #using dead end cells, look for dead end routes 
    while count != 0:
        counter = 0
        for i in range(mapSize[0]):
            for j in range(mapSize[1]):
                dirBlock = [0, 0, 0, 0]
                sumBlock = 0
                neighborLoc = [i, j]
                for k in [1, 2, 3, 4]:
                    dirStat = gridmap.getNeighborObstacle(i, j, k)
                    if dirStat == 0:
                        #check in skipCells list 
                        if k == 3:
                            #south
                            neighborCheck = [i+1, j]
                        elif k == 1:
                            #north
                            neighborCheck = [i-1, j]
                        elif k == 2:
                            #east
                            neighborCheck = [i, j+1]
                        else:
                            #west
                            neighborCheck = [i, j-1]  
                        if neighborCheck in skipCells:
                            dirStat = 1
                    dirBlock[k-1] = dirStat
                for s in range(len(dirBlock)):
                    if dirBlock[s] != 0:
                        sumBlock = sumBlock + 1
                if sumBlock >= 3:
                    if i == xs[0] and j == xs[1]:
                        pass
                    elif i == xg[0] and j == xg[1]:
                        pass
                    elif [i, j] in skipCells:
                        pass
                    else: 
                        skipCells.append(neighborLoc)
                        counter = counter+1
                        gridmap.setCost(neighborLoc[0], neighborLoc[1], deadCost)
            count = counter
            counter = 0
    deadCellCount = len(skipCells)
    return skipCells


def costProp(xs, xg, skipCells):
    # generate the map
    gridmap.printObstacleMap()

    initCost = -1
    blockedSquares = len(skipCells)


    for i in range(8):
        for j in range(8):
            gridmap.setCost(i, j, initCost)

    cost = 0
    gridmap.setCost(xs[0], xs[1], cost)
    #for known map only: 
    availSquares = (8*8)-1 #initating all but start pos as available squares 

    pos = [xs[0], xs[1]]
    counting = 0
    while availSquares > blockedSquares:
        counting = counting +1
        if xs[0] == xg[0] and xs[1] == xg[1]:
            break
        if counting > (8*8)*1000:
            break
        for i in range(8):
            for j in range(8):
                if pos != [xg[0], xg[1]]:
                    if gridmap.getCost(pos[0], pos[1]) == cost:
                        for k in dirs:
                            if gridmap.getNeighborObstacle(pos[0], pos[1], k) == 0:
                                if k == 3:
                                    #south
                                    neighborPos = [pos[0]+1, pos[1]]
                                elif k == 1:
                                    #north
                                    neighborPos = [pos[0]-1, pos[1]]
                                elif k == 2:
                                    #east
                                    neighborPos = [pos[0], pos[1]+1]
                                else:
                                    #west
                                    neighborPos = [pos[0], pos[1]-1]  
                                if gridmap.getCost(neighborPos[0], neighborPos[1]) == -1:
                                    if neighborPos in skipCells:
                                        pass
                                    else: 
                                        gridmap.setCost(neighborPos[0], neighborPos[1], cost+1)
                                        availSquares = availSquares - 1
                pos = [i, j]
        cost = cost + 1
    gridmap.printCostMap()

def pathFind(xs, xg):
    endCellCost = gridmap.getCost(xg[0], xg[1])
    if endCellCost == -1:
        print("Cannot be pathed")
        pathYN = 0
        pathing = 0
    else:
        print("End Cell Cost: ", endCellCost)
        costGrad = endCellCost
        pos = [xg[0], xg[1]]
        pathing = [pos]
        counting = 0
        while costGrad > 0: 
            counting = counting +1
            if counting > (8*8)+1000:
                print("Cannot be pathed")
                break
            for i in range(8):
                for j in range(8):
                    if gridmap.getCost(pos[0], pos[1]) == costGrad:
                        for k in dirs:
                            if gridmap.getNeighborObstacle(i, j, k) == 0:
                                if k == 3:
                                    #south
                                    nextPos = [pos[0]+1, pos[1]]
                                elif k == 1:
                                    #north
                                    nextPos = [pos[0]-1, pos[1]]
                                elif k == 2:
                                    #east
                                    nextPos = [pos[0], pos[1]+1]
                                else:
                                    #west
                                    nextPos = [pos[0], pos[1]-1]  
                                if nextPos[0] < 8 and nextPos[0] >= 0: 
                                    if nextPos[1] <8 and nextPos[1] >= 0:
                                        if gridmap.getCost(nextPos[0], nextPos[1]) == costGrad-1:
                                            testBlock = [nextPos[0] - pos[0], nextPos[1] - pos[1]]
                                            if testBlock == [1, 0]:
                                                neighCheck = gridmap.getNeighborObstacle(pos[0], pos[1], 3)
                                            elif testBlock == [-1, 0]:
                                                neighCheck = gridmap.getNeighborObstacle(pos[0], pos[1], 1)
                                            elif testBlock == [0, 1]:
                                                neighCheck = gridmap.getNeighborObstacle(pos[0], pos[1], 2)
                                            elif testBlock == [0,-1]:
                                                neighCheck = gridmap.getNeighborObstacle(pos[0], pos[1], 4)
                                            if pos == [xs[0], xs[1]]:
                                                break
                                            if neighCheck == 0:
                                                pathing.append(nextPos)
                                                costGrad = costGrad -1 
                                                pos = nextPos
                                            else: 
                                                pass
                                            
        print("Path Steps: ", pathing)
        pathYN = 1
    return [pathYN, pathing]

def pathFollowingCommands(xs, xg, pathYN, path):
    if pathYN == 1:
        headingDir = xs[2]
        for jj in range(len(path)):
            index = len(path)-1-jj
            if index == 0:
                pass
            else: 
                headingDir = headingDir
                print("step: ", jj+1)
                print(path[index])
                print (path[index-1])
                pos1 = path[index]
                pos2 = path[index-1]
                headingChange = [pos2[1]-pos1[1], pos2[0]-pos1[0]]
                if headingDir == 3:
                    print("Facing South")
                    if headingChange == [1, 0]:
                        print("left, east")
                        leftTurn()
                        headingDir = 2
                    elif headingChange == [-1, 0]:
                        print("right, west")
                        rightTurn()
                        headingDir = 4
                    elif headingChange == [0, 1]:
                        print("none, south")
                        headingDir = 3
                    else: 
                        print("turn around, north")
                        turnAround()
                        headingDir = 1
                elif headingDir == 1:
                    print("Facing North")
                    if headingChange == [1, 0]:
                        print("right, east")
                        rightTurn()
                        headingDir = 2
                    elif headingChange == [-1, 0]:
                        print("left, west")
                        leftTurn()
                        headingDir = 4
                    elif headingChange == [0, 1]:
                        print("turn around, south")
                        turnAround()
                        headingDir = 3
                    else: 
                        print("none, north")
                        headingDir = 1
                elif headingDir == 2:
                    print("Facing East")
                    if headingChange == [1, 0]:
                        print("none, east")
                        headingDir = 2
                    elif headingChange == [-1, 0]:
                        print("turn around, west")
                        turnAround()
                        headingDir = 4
                    elif headingChange == [0, 1]:
                        print("right, south")
                        rightTurn()
                        headingDir = 3
                    else: 
                        print("left, north")
                        leftTurn()
                        headingDir = 1
                else: 
                    print("Facing West")
                    if headingChange == [1, 0]:
                        print("turn around, east")
                        turnAround()
                        headingDir = 2
                    elif headingChange == [-1, 0]:
                        print("none, west")
                        headingDir = 4
                    elif headingChange == [0, 1]:
                        print("left, south")
                        leftTurn()
                        headingDir = 3
                    else: 
                        print("right, north")
                        rightTurn()
                        headingDir = 1
                singleCell()
        if headingDir != xg[2]:
            headingChange = xg[2]
            if headingDir == 3:
                print("Facing South")
                if headingChange == 2:
                    print("left, east")
                    leftTurn()
                    headingDir = 2
                elif headingChange == 4:
                    print("right, west")
                    rightTurn()
                    headingDir = 4
                elif headingChange == 3:
                    print("none, south")
                    headingDir = 3
                else: 
                    print("turn around, north")
                    turnAround()
                    headingDir = 1
            elif headingDir == 1:
                print("Facing North")
                if headingChange == 2:
                    print("right, east")
                    rightTurn()
                    headingDir = 2
                elif headingChange == 4:
                    print("left, west")
                    leftTurn()
                    headingDir = 4
                elif headingChange == 3:
                    print("turn around, south")
                    turnAround()
                    headingDir = 3
                else: 
                    print("none, north")
                    headingDir = 1
            elif headingDir == 2:
                print("Facing East")
                if headingChange == 2:
                    print("none, east")
                    headingDir = 2
                elif headingChange == 4:
                    print("turn around, west")
                    turnAround()
                    headingDir = 4
                elif headingChange == 3:
                    print("right, south")
                    rightTurn()
                    headingDir = 3
                else: 
                    print("left, north")
                    leftTurn()
                    headingDir = 1
            else: 
                print("Facing West")
                if headingChange == 2:
                    print("turn around, east")
                    turnAround()
                    headingDir = 2
                elif headingChange == 4:
                    print("none, west")
                    headingDir = 4
                elif headingChange == 3:
                    print("left, south")
                    leftTurn()
                    headingDir = 3
                else: 
                    print("right, north")
                    rightTurn()
                    headingDir = 1
        print("Done!")
    else: 
        print("No commands sent")

def pathFollowing(gridmap):
    xsi = int(input("Input Start Position i: "))
    if xsi < 0 or xsi >= 8:
        while xsi < 0 or xsi >= 8:
            xsi = int(input("Invalid Input, Input Start Position i: "))
    xsj = int(input("Input Start Position j: "))
    if xsj < 0 or xsj >= 8:
        while xsj < 0 or xsj >= 8:
            xsj = int(input("Invalid Input, Input Start Position j: "))
    xstheta = int(input("Input Start Position k: "))
    if xstheta <= 0 or xstheta > 4:
        while xstheta <= 0 or xstheta > 4:
            xstheta = int(input("Invalid Input, Input Start Position k: "))
    xgi = int(input("Input End Position i: "))
    if xgi < 0 or xgi >= 8:
        while xgi < 0 or xgi >= 8:
            xgi = int(input("Invalid Input, Input End Position i: "))
    xgj = int(input("Input End Position j: "))
    if xgj < 0 or xgj >= 8:
        while xgj < 0 or xgj >= 8:
            xgj = int(input("Invalid Input, Input End Position j: "))
    xgtheta = int(input("Input End Position k: "))
    if xgtheta <= 0 or xgtheta > 4:
        while xgtheta <= 0 or xgtheta > 4:
            xgtheta = int(input("Invalid Input, Input End Position k: "))
    xs = [xsi, xsj, xstheta]
    xg = [xgi, xgj, xgtheta]
    timeStart = time.time()
    print("Start: ", xs)
    print("End: ", xg)
    nskip = deadCells(xs, xg)
    costProp(xs, xg, nskip)
    [pathYN, path] = pathFind(xs, xg)
    pathFollowingCommands(xs, xg, pathYN, path)
    print("Elapsed time(s): ", (time.time()-timeStart))
    return timeStart


def checkSensors():
    # set the threshold values for the sensors 
    # thresh_left_high = 800
    thresh_left_low = 200

    # thresh_right_high = 800
    thresh_right_low = 200

    # thresh_front_high = 3000
    thresh_front_low = 1500

    front_sensor_val = getSensorValue(2) # check later
    right_sensor_val = getSensorValue(4) # check sensor ID
    left_sensor_val = getSensorValue(3) # check sensor ID

    print("front sensor", front_sensor_val)
    print("left sensor", left_sensor_val)
    print("right sensor", right_sensor_val)

    sensorsBlocked = []

    if (left_sensor_val >= thresh_left_low):
        sensorsBlocked.append(True)
    else:
        sensorsBlocked.append(False)

    if (right_sensor_val >= thresh_right_low):
        sensorsBlocked.append(True)
    else:
        sensorsBlocked.append(False)
    
    if (front_sensor_val >= thresh_front_low):
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
            # possible_turn_commands = ["Forward","Right"]
            possible_turn_commands = ["Forward"]
            # print("Turn command is: ", turn_command)
            for command in possible_turn_commands:
                suggested_headings.append(turn2NewPos(command,current_pos)[2])
                suggested_pos_list.append(turn2NewPos(command,current_pos))

        elif (sensorsBlocked[0] is False) and (sensorsBlocked[1] is True) and (sensorsBlocked[2] is False):
            # only right sensor blocked -> can go forward OR left
            # possible_turn_commands = ["Left","Forward"]
            possible_turn_commands = ["Forward"]
            for command in possible_turn_commands:
                suggested_headings.append(turn2NewPos(command,current_pos)[2])
                suggested_pos_list.append(turn2NewPos(command,current_pos))
            
        elif (sensorsBlocked[0] is False) and (sensorsBlocked[1] is False) and (sensorsBlocked[2] is True):
            # only front sensor blocked -> can go left OR right
            # possible_turn_commands = ["Left","Right"]
            possible_turn_commands = ["Left","Right"]
            for command in possible_turn_commands:
                suggested_headings.append(turn2NewPos(command,current_pos)[2])
                suggested_pos_list.append(turn2NewPos(command,current_pos))
        
        else:
            # if no sensors blocked but cell visited before,
            # choose a random heading based on headings not yet visited
            # COME BACK TO THIS!
            # possible_turn_commands = ["Forward","Left","Right"]
            possible_turn_commands = ["Forward"]
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
            # possible_turn_commands = ["Forward","Right"]
            possible_turn_commands = ["Forward"]
            turn_command = possible_turn_commands.pop(0)
            # print("Turn command is: ", turn_command)
            next_pos = turn2NewPos(turn_command,current_pos)
            next_heading = turn2NewPos(turn_command,current_pos)[2]

        elif (sensorsBlocked[0] is False) and (sensorsBlocked[1] is True) and (sensorsBlocked[2] is False):
            # only right sensor blocked -> can go forward OR left
            # possible_turn_commands = ["Left","Forward"]
            possible_turn_commands = ["Forward"]
            turn_command = possible_turn_commands.pop(0)
            next_pos = turn2NewPos(turn_command,current_pos)
            next_heading = turn2NewPos(turn_command,current_pos)[2]
            
        elif (sensorsBlocked[0] is False) and (sensorsBlocked[1] is False) and (sensorsBlocked[2] is True):
            # only front sensor blocked -> can go left OR right
            # possible_turn_commands = ["Left","Right"]
            possible_turn_commands = ["Left","Right"]
            turn_command = possible_turn_commands.pop(0) # take the first element
            next_pos = turn2NewPos(turn_command,current_pos)
            next_heading = turn2NewPos(turn_command,current_pos)[2]

        # update all moves with the new move & make a return  
        else:
            # no sensors blocked, choose a direction randomly if new cell
            # but prevent from going back where it came
            # possible_turn_commands = ["Forward","Left","Right"]
            possible_turn_commands = ["Forward"]
            turn_command = random.choice(possible_turn_commands)
            next_pos = turn2NewPos(turn_command,current_pos)
            next_heading = turn2NewPos(turn_command,current_pos)[2]
        
    moves_list.append(next_pos)
    return next_pos

def correctiveTurn(sensorsBlocked):
    lsensor = sensorsBlocked[0]
    rsensor = sensorsBlocked[1]

    lthresh = 700
    rthresh = 700

    if lsensor > lthresh:
        print("completing right corrective turn")
        setMotorMode(motor1,1)
        setMotorMode(motor2,1)
        setMotorMode(motor3,1)
        setMotorMode(motor4,1)

        end_time = time.time() + 1 # 5 seconds later

        while time.time() < end_time:
            setMotorWheelSpeed(motor1, 300)
            setMotorWheelSpeed(motor2, 300)
            setMotorWheelSpeed(motor3, 300)
            setMotorWheelSpeed(motor4, 300)
        setMotorWheelSpeed(motor1, 0)
        setMotorWheelSpeed(motor2, 0)
        setMotorWheelSpeed(motor3, 0)
        setMotorWheelSpeed(motor4, 0)
        
    elif rsensor > rthresh:
        print("completing left corrective turn")
        setMotorMode(motor1,1)
        setMotorMode(motor2,1)
        setMotorMode(motor3,1)
        setMotorMode(motor4,1)
        
        end_time = time.time() + 3 # 5 seconds later

        while time.time() < end_time:
            setMotorWheelSpeed(motor1, 300+1024)
            setMotorWheelSpeed(motor2, 300+1024)
            setMotorWheelSpeed(motor3, 300+1024)
            setMotorWheelSpeed(motor4, 300+1024)
        setMotorWheelSpeed(motor1, 0)
        setMotorWheelSpeed(motor2, 0)
        setMotorWheelSpeed(motor3, 0)
        setMotorWheelSpeed(motor4, 0)
    else:
        pass


# based on information on the past state and next state, move the robot
def moveRobot(current_pos,sensorsBlocked, next_pos,robot_not_moved):
    # compare values of i,j,k in both states, if they are the same, robot should not move:
    fsensor = sensorsBlocked[2]
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
                if fsensor > 3000:
                    pass
                else:
                    print("go forward")
                    correctiveTurn(sensorsBlocked)
                    singleCell()
                    
            else:
                print("don't move")
                robot_not_moved += 1
        else:
            if ((k_past == DIRECTION.North) and (k_next == DIRECTION.South)) or \
            ((k_past == DIRECTION.South) and (k_next == DIRECTION.North)) or \
            ((k_past == DIRECTION.East) and (k_next == DIRECTION.West)) or \
            ((k_past == DIRECTION.West) and (k_next == DIRECTION.East)):
            # a 180 degree turn is desired
                turnAround()
                print("Turn around")

            else:
                # a 90 degree turn is desired
                orientation_diff = k_next - k_past
                if (k_past == DIRECTION.North) or (k_next == DIRECTION.North):
                    if orientation_diff == 3:
                        # the turn occurs from North to West i.e. a left turn
                        leftTurn() 
                        print("left turn")

                    elif (orientation_diff > 0) and (orientation_diff < 3):
                        print("right turn")
                        rightTurn()

                    elif (orientation_diff > -3) and (orientation_diff < 0):
                        print("left turn")
                        leftTurn()

                    elif (orientation_diff == -3):
                        # the turn occurs from West to North, i.e. a right turn
                        # rightTurn() # uncomment later
                        print("right turn")
                        rightTurn()
                    else:
                        print('Error in moveRobot: Unknown or illegal combination of turns')
                
                else:
                    if orientation_diff < 0:
                        # turn occured in the anticlockwise direction i.e. left turn
                        print("left turn")
                        leftTurn()
                    else:
                        # turn occured in the clockwise direction i.e. right turn
                        print("right turn")
                        rightTurn()


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
            print("Facing South: left wall blocked")
            obstacle_map.setObstacle(i,j,isBlocked,obstacle_dir)

        if rsensor_blocked is True:
            obstacle_dir = DIRECTION.West
            isBlocked = 1
            print("Facing South: right wall blocked")
            obstacle_map.setObstacle(i,j,isBlocked,obstacle_dir)
        
        if fsensor_blocked is True:
            obstacle_dir = DIRECTION.South
            isBlocked = 1
            print("Facing South: front wall blocked")
            obstacle_map.setObstacle(i,j,isBlocked,obstacle_dir)

    # if robot is heading north
    elif dir == DIRECTION.North:
        if lsensor_blocked is True:
            obstacle_dir = DIRECTION.West
            isBlocked = 1
            obstacle_map.setObstacle(i,j,isBlocked,obstacle_dir)
            print("Facing North: left wall blocked")

        if rsensor_blocked is True:
            obstacle_dir = DIRECTION.East
            isBlocked = 1
            obstacle_map.setObstacle(i,j,isBlocked,obstacle_dir)
            print("Facing North: right wall blocked")
        
        if fsensor_blocked is True:
            obstacle_dir = DIRECTION.North
            isBlocked = 1
            obstacle_map.setObstacle(i,j,isBlocked,obstacle_dir)
            print("Facing North: front wall blocked")
    
    # if robot is heading east
    elif dir == DIRECTION.East:
        if lsensor_blocked is True:
            obstacle_dir = DIRECTION.North
            isBlocked = 1
            obstacle_map.setObstacle(i,j,isBlocked,obstacle_dir)
            print("Facing East: left wall blocked")


        if rsensor_blocked is True:
            obstacle_dir = DIRECTION.South
            isBlocked = 1
            obstacle_map.setObstacle(i,j,isBlocked,obstacle_dir)
            print("Facing East: right wall blocked")
        
        if fsensor_blocked is True:
            obstacle_dir = DIRECTION.East
            isBlocked = 1
            obstacle_map.setObstacle(i,j,isBlocked,obstacle_dir)
            print("Facing East: front wall blocked")

    # if robot is heading west
    elif dir == DIRECTION.West:
        if lsensor_blocked is True:
            obstacle_dir = DIRECTION.South
            isBlocked = 1
            obstacle_map.setObstacle(i,j,isBlocked,obstacle_dir)
            print("Facing West: left wall blocked")

        if rsensor_blocked is True:
            obstacle_dir = DIRECTION.North
            isBlocked = 1
            obstacle_map.setObstacle(i,j,isBlocked,obstacle_dir)
            print("Facing West: right wall blocked")

        if fsensor_blocked is True:
            obstacle_dir = DIRECTION.West
            isBlocked = 1
            obstacle_map.setObstacle(i,j,isBlocked,obstacle_dir)
            print("Facing West: front wall blocked")
    
    else:
        print('Error in updateMaps: Unknown value of DIRECTION entered.')

def mapping(startPos, max_time):
    all_moves = {}
    moves_list = []
    pos = startPos

    obstacle_map = EECSMap()
    obstacle_map.clearObstacleMap()
    obstacle_map.printObstacleMap()
    # sensorsBlocked = checkSensors()
    # print(sensorsBlocked)
    # for combination in sensorsBlocked:
    robot_not_moved = 0 # initialize counter
    # current_time = time.time()

    # while time.time() < (current_time + 30): # while the robot hasn't been stationary for more than 4 iterations
    ending_time = time.time() + max_time
    start_time = time.time()
    while (robot_not_moved < 3) or (time.time() < ending_time):

        sensorsBlocked = checkSensors()
        updateMap(obstacle_map,sensorsBlocked,pos)
        robot_not_moved += 1
        next_pos = decideNextMove(all_moves,pos,sensorsBlocked,moves_list)
        print("next pos: ", next_pos)
        print("moves list: ", moves_list)
        robot_not_moved = moveRobot(pos,sensorsBlocked,next_pos,robot_not_moved)

        next_pos_only = (next_pos[0],next_pos[1])
        next_heading = next_pos[2]
        if next_pos_only in all_moves.keys():
            if next_heading not in all_moves[next_pos_only]:
                all_moves[next_pos_only].append(next_heading)
        else:
            all_moves.update({next_pos_only:[next_heading]})

        pos = next_pos
    print("Elapsed time(s): ", (time.time()-start_time))
    print("Ending exploration.")
    obstacle_map.printObstacleMap()
    unique_cells = len(all_moves.keys())
    print("The robot arrived at ", unique_cells, " unique cells.")
    print("Percentage of the map traveled: ", float(unique_cells/64)*100)

    return obstacle_map

# Main function
if __name__ == "__main__":
    rospy.init_node('example_node', anonymous=True)
    rospy.loginfo("Starting Group X Control Node...")  

    mode = input("Program Modes: \n1: Path Following\n2: Map Building\n")
    if mode == 1: 
        print("Path Following Mode")
        gridmap = EECSMap()
        pathFollowing(gridmap)
    elif mode == 2:
        print("Map Building Mode")
        path_map = input("Should the robot path the generated map? Y: 1, N: 0 ")
        max_time = input("Max Time for Robot Mapping (in seconds): ")
        i = input("Robot start position i: ")
        j = input("Robot start position j: ")
        k =  input("Robot start position k (N = 1; E = 2; S = 3; W = 4): ")

        startPos = (i,j,k)

        if path_map == 0:
            mapping(startPos,max_time)
        elif path_map == 1:
            gridmap = mapping(startPos,max_time)
            pathFollowing(gridmap)
        else:
            print("Invalid input.")

    else: 
        print("Restart, no mode selected")
        rightTurn()
        # leftTurn()

    # gridmap = EECSMap()
    # gridmap.printObstacleMap()

    # setMotorMode(motor1,1)
    # setMotorMode(motor2,1)
    # setMotorMode(motor3,1)
    # setMotorMode(motor4,1)

                      
# all_moves = {}
# moves_list = []
# pos = (0,6,2)

# # front_sensor_val = getSensorValue(2) # check later
# # right_sensor_val = getSensorValue(4) # check sensor ID
# # left_sensor_val = getSensorValue(3) # check sensor ID

# # print("front sensor", front_sensor_val)
# # print("left sensor", left_sensor_val)
# # print("right sensor", right_sensor_val)







    #south = 3
    #north = 1
    #east = 2 
    #west = 4 
    # mode = 0
    # mode = input("Program Modes: \ne: Path Following\ng: Map Building\n")
    # if mode == 'e': 
    #     print("Path Following Mode")
    #     pathFollowing()
    # elif mode == 'g':
    #     print("Map Building Mode")
    # else: 
    #     print("Restart, no mode selected")

    # timeStart = pathFollowing()
    # endTime = time.time()
    # print("Time to Execute: ", endTime-timeStart)
    #leftTurn()

    # control loop running at 10hz
    # r = rospy.Rate(0.5) # 10hz
    # while not rospy.is_shutdown():
	
    #     # sleep to enforce loop rate
        #r.sleep()


