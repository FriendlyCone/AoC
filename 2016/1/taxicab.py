with open("input.txt", "r") as inputfile:
    #Reading the input file
    stepList = inputfile.read().split(sep=", ")
    # stepList = [step.strip() for step in stepList]
    
print(stepList)
xAxis = 0 # + North - South
yAxis = 0 # + East - West

# Track what the max highs and lows are per axis to determine grid size
xAxisUpper = 0
xAxisLower = 0
yAxisUpper = 0
yAxisLower = 0

# Challenge specifies that initial starting direction is North, since I want to needlessly visually show the grid that is relevant.
currentFacing = 0

# Every instruction is 2 characters, a direction / rotation and how many blocks to move there.
# Make some characters to represent the faced direction
directionList = ["^", ">", "v", "<"]
totalDistance = 0

for step in stepList:
    direction = step[0]
    distance = int(step[1:])
    print(f"We're moving {direction} for {distance} blocks.")
    if direction == "L":
        rotation = -1
    else:
        rotation = 1
    currentFacing += rotation
    # Ensure list rollover
    if currentFacing == -1:
        currentFacing = 3
    elif currentFacing == 4:
        currentFacing = 0
    print(f"We're facing {directionList[currentFacing]}")
    #  Since the actual bends don't matter currently just getting the total distance per axis is fine
    if currentFacing == 0:
        xAxis += distance
    elif currentFacing == 2:
        xAxis -= distance
    elif currentFacing == 1:
        yAxis += distance
    elif currentFacing == 3:
        yAxis -= distance
    print(f"North = {xAxis}, East = {yAxis}")
    if xAxis < 0:
        xAxisDist = xAxis * -1
    else:
        xAxisDist = xAxis
    if yAxis < 0:
        yAxisDist = yAxis * -1
    else: 
        yAxisDist = yAxis
    print(f"xAxis = {xAxisDist}, yAxis = {yAxisDist}")
    totalDistance = xAxisDist + yAxisDist
    print(totalDistance)
    
# To know the if we go somewhere twice we need to make a grid now

