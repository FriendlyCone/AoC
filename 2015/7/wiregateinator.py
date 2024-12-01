with open("test.txt", "r") as inputfile:
# with open("input.txt", "r") as inputfile:
    input = inputfile.read().splitlines()
    input = [command.split(" ") for command in input]

circuitionary = {}

# Make sure every wire is in the dictionary
for command in input:
    for item in command:
        if item.isalpha() and item.islower():
            if item not in circuitionary:
                circuitionary[item] = 0
    print(command)

def operatorinator(circuitionary, input):
    for command in input:
        print(command)
        if "AND" in command or "OR" in command:
            # AND = &
            # af AND ah -> ai
            # OR = |
            # af AND ah -> ai
            x = command[0]
            if x.isnumeric():
                xval = int(x)
            else:
                if circuitionary.get(x) == 0:
                    print("This value is still 0")
                    continue
                xval = circuitionary.get(x)
            y = command[2]
            if y.isnumeric():
                yval = int(y)
            else:
                if circuitionary.get(y) == 0:
                    print("This value is still 0")
                    continue
                yval = circuitionary.get(y)
            a = command[4]
            if "AND" in command:
                aval = xval & yval
            else:
                aval = xval | yval
            circuitionary[a] = aval

        elif "NOT" in command:
            # NOT = ~
            # NOT lk -> ll
            x = command[1]
            if x.isnumeric():
                xval = int(x)
            else:
                if circuitionary.get(x) == 0:
                    print("This value is still 0")
                    continue
                xval = circuitionary.get(x)
            a = command[3]
            aval = ~xval
            circuitionary[a] = aval

        elif "LSHIFT" in command or "RSHIFT" in command:
            # LSHIFT = <<
            # eo LSHIFT 15 -> es
            # RSHIFT = >>
            # hz RSHIFT 1 -> is
            x = command[0]
            if x.isnumeric():
                xval = int(x)
            else:
                if circuitionary.get(x) == 0:
                    print("This value is still 0")
                    continue
                xval = circuitionary.get(x)
            y = command[2]
            if y.isnumeric():
                yval = int(y)
            else:
                if circuitionary.get(y) == 0:
                    print("This value is still 0")
                    continue
                yval = circuitionary.get(y)
            a = command[4]
            if "LSHIFT" in command:
                aval = xval << yval
            else:
                aval = xval >> yval
            circuitionary[a] = aval

        else:
            # Basic value set
            # 0 -> c
            x = command[0]
            if x.isnumeric():
                xval = int(x)
            else:
                if circuitionary.get(x) == 0:
                    print("This value is still 0")
                    continue
                xval = circuitionary.get(x)
            a = command[2]
            aval = xval
            circuitionary[a] = aval
    return circuitionary
        
finalcircuitionary = circuitionary.copy()
done = False
while not done:
    print("inserting")
    circuitionary = operatorinator(circuitionary, input)
    if finalcircuitionary == circuitionary:
        print("Totally done now fo sho")
        done = True
    else:
        finalcircuitionary = circuitionary.copy()
        print(finalcircuitionary)

print(finalcircuitionary)