import numpy

with open("input.txt", "r") as inputfile:
    instructionList = inputfile.read().splitlines()
    instructionListFixed = []
    for instruction in instructionList:
        instruction = instruction.replace("turn on", "on")
        instruction = instruction.replace("turn off", "off")
        instruction = instruction.replace("through ", "")
        part1, part2, part3 = instruction.split(" ")
        instructionListFixed.append([part1, part2, part3])

# We're working with a 1000x1000 grid, which translates to 0-999x0-999 since we start at 0
# Generate grid
rows, columns = 1000, 1000
rawgrid = [[0]*columns]*rows
grid = numpy.array(rawgrid)
gridbasic = numpy.copy(grid)
gridextreme = numpy.copy(grid)

# Part one setup
def lightinator(lightcommand, lightstart, lightend, lightgrid):
    startL = lightstart.split(",")
    startX = int(startL[0])
    startY = int(startL[1])
    endL = lightend.split(",")
    endX = int(endL[0])
    endY = int(endL[1])
    while startX <= endX:
        startYticker = startY
        while startYticker <= endY:
            if lightcommand == "on":
                lightgrid[startX,startYticker] = 1
            elif lightcommand == "off":
                lightgrid[startX,startYticker] = 0
            elif lightcommand == "toggle":
                if lightgrid[startX,startYticker] == 0:
                    lightgrid[startX,startYticker] = 1
                else: 
                    lightgrid[startX,startYticker] = 0
            else:
                print("WTF")
                return
            startYticker = startYticker + 1
        startX = startX + 1
    return lightgrid

# Part one setup
def lightinatorextreme(lightcommand, lightstart, lightend, lightgrid):
    startL = lightstart.split(",")
    startX = int(startL[0])
    startY = int(startL[1])
    endL = lightend.split(",")
    endX = int(endL[0])
    endY = int(endL[1])
    while startX <= endX:
        startYticker = startY
        while startYticker <= endY:
            if lightcommand == "on":
                lightgrid[startX,startYticker] = lightgrid[startX,startYticker] + 1
            elif lightcommand == "off":
                if lightgrid[startX,startYticker] == 0:
                    pass
                else:
                    lightgrid[startX,startYticker] = lightgrid[startX,startYticker] - 1
            elif lightcommand == "toggle":
                lightgrid[startX,startYticker] = lightgrid[startX,startYticker] + 2
            else:
                print("WTF")
                return
            startYticker = startYticker + 1
        startX = startX + 1
    return lightgrid

# Main loop
for instruction in instructionListFixed:
    gridbasic = lightinator(instruction[0], instruction[1], instruction[2], gridbasic)
    gridextreme = lightinatorextreme(instruction[0], instruction[1], instruction[2], gridextreme)

# Find how many 1's we end up with
activelights = 0
totalbrightness = 0

# Get basic activelights
with numpy.nditer(gridbasic) as lightgrid:
    for light in lightgrid:
        activelights = activelights + light

# Get extreme totalbrightness
with numpy.nditer(gridextreme) as lightgrid:
    for light in lightgrid:
        totalbrightness = totalbrightness + light

print(f"The number of active lights is {activelights}")
print(f"The total brightness is {totalbrightness}")