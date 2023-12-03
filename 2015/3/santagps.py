with open("input.txt", "r") as inputfile:
    directionList = [*inputfile.read()]

# Dictionary time?!?!
# x0y0 : numberpresent
# This one is super overcomplicated because I expected that Part 2 would require using the specific coords, turns out you don't need them at all ah well

# Starting pos
x = 0 # left = -1 right = +1
y = 0 # down = -1 up = +1
gpsHistory = {}

# Part one
print("Processing steps...")
for direction in directionList:
    if direction == "^":
        y = y + 1
    elif direction == "v":
        y = y - 1
    elif direction == ">":
        x = x + 1
    elif direction == "<":
        x = x - 1
    # gridlocation = f"x{x}y{y}"
    gridlocation = f"{x}_{y}"
    if gridlocation in gpsHistory:
        newvalue = gpsHistory[gridlocation] + 1
        gpsHistory[gridlocation] = newvalue
        print("+", end="")
    else:
        gpsHistory[gridlocation] = 1
        print("-", end="")
    
print(f"\nSanta made {len(gpsHistory)} unique stops, which therefore have atleast 1 gift.")

# Part two
# Starting pos
xs = 0 # left = -1 right = +1
ys = 0 # down = -1 up = +1
xr = 0 # left = -1 right = +1
yr = 0 # down = -1 up = +1
gpsHistorywithRobo = {}
instructioncount = 0

print("Processing steps...")
for direction in directionList:
    # Choose Santa or RoboSanta
    if instructioncount % 2 == 0:
        x, y = xs, ys
    else:
        x, y = xr, yr
    
    #Proceed as usual
    if direction == "^":
        y = y + 1
    elif direction == "v":
        y = y - 1
    elif direction == ">":
        x = x + 1
    elif direction == "<":
        x = x - 1
    # gridlocation = f"x{x}y{y}"
    gridlocation = f"{x}_{y}"
    if gridlocation in gpsHistorywithRobo:
        newvalue = gpsHistorywithRobo[gridlocation] + 1
        gpsHistorywithRobo[gridlocation] = newvalue
        print("+", end="")
    else:
        gpsHistorywithRobo[gridlocation] = 1
        print("-", end="")
    
    # Store value again
    if instructioncount % 2 == 0:
        xs, ys = x, y
    else:
        xr, yr = x, y
    instructioncount = instructioncount + 1
    
print(f"\nSanta and RoboSanta made {len(gpsHistorywithRobo)} unique stops, which therefore have atleast 1 gift.")