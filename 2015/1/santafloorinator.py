#Open input the correct way
with open("input.txt", "r") as inputfile:
    #Reading the input file
    stepList = [*inputfile.read()]

# ( = up one floor
# ) = down one floor
# starting floor = 0

#Variables
currentfloor = 0
stepcount = 0
firstbasement = 0
foundfirst = False

print("What floor do we end up on?")
for direction in stepList:
    #Count steps for part 2 so we know what step we're on
    stepcount = stepcount + 1

    #Move up and down based on character
    if direction == "(":
        currentfloor = currentfloor + 1
        print("+", end="")
    elif direction == ")":
        currentfloor = currentfloor - 1
        print("-", end="")

    # Check if we're on floor -1 and haven't already found the first time we enter the basement
    if currentfloor == -1 and not foundfirst:
        firstbasement = stepcount
        foundfirst = True

print(f"\nWe end up on floor {currentfloor}")
print(f"We entered the basement at step {firstbasement}")