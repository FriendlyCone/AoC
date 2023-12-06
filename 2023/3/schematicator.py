with open("input.txt", "r") as inputfile:
    schematic = []
    for line in inputfile:
        column = [*line.strip()]
        schematic.append(column)

def partfinder(schematic):
    partList = []
    numberlength = 0
    number = ""
    coordX = 0
    coordY = 0
    processing = False
    for x in schematic:
        for y in x:
            if y.isnumeric():
                numberlength = numberlength + 1
                number = number + y
                if not processing:
                    processing = True
                    digitcoordYstart = coordY
            if numberlength > 0 and not y.isnumeric():
                print(f"\nFound whole number {number}, it is {numberlength} digits.")
                print(f"The X is {coordX}, the Y range is {digitcoordYstart} to {digitcoordYstart+numberlength-1}")
                if checkifpartnumber(schematic, coordX, digitcoordYstart, numberlength):
                    partList.append(int(number))
                numberlength = 0
                number = ""
                processing = False
            coordY = coordY + 1
        coordY = 0
        coordX = coordX + 1
    return partList

def checkifpartnumber(schematic, coordX, startY, numberlength):
    specialList = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "/", "\\"]
    for x in range(-1, 2, 1):
        if coordX+x >= 0 and coordX+x <= len(schematic)-1:
            pass
        else:
            continue
        for y in range(startY-1, startY+numberlength+1, 1):
            if y >= 0 and y <= len(schematic[0])-1:
                print(f"{schematic[coordX+x][y]}", end="")
                pass
            else:
                continue
            if schematic[coordX+x][y] in specialList:
                print(f"\nConfirmed it is a part: {schematic[coordX+x][y]}")
                return True
        print("\n", end="")
    return False

def gearfinder(schematic):
    gearList = []
    specialList = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "/", "\\"]
    special = ""
    coordX = 0
    coordY = 0
    for x in schematic:
        for y in x:
            if y in specialList:
                special = y
                print(f"\nFound special character {special}.")
                print(f"The X is {coordX}, the Y is {coordY}")
                isGear, gear = checkifgear(schematic, coordX, coordY)
                if isGear:
                    gearList.append(int(gear))
                special = ""
            coordY = coordY + 1
        coordY = 0
        coordX = coordX + 1
    return gearList

def checkifgear(schematic, coordX, coordY):
    gear = 0
    foundDigits = 0
    numberstoFind = []
    for x in range(-1, 2, 1):
        gap = True
        if coordX+x >= 0 and coordX+x <= len(schematic)-1:
            pass
        else:
            continue
        for y in range(coordY-1, coordY+2, 1):
            if y >= 0 and y <= len(schematic[0])-1:
                print(f"{schematic[coordX+x][y]}", end="")
                pass
            else:
                continue
            if schematic[coordX+x][y].isnumeric() and gap:
                numberstoFind.append([coordX+x, y])
                foundDigits = foundDigits + 1
                gap = False
            elif not schematic[coordX+x][y].isnumeric():
                gap = True
        print("\n", end="")
    if foundDigits == 2:
        print("Found exactly 2 attached numbers.")
        gear = numberator(schematic, numberstoFind)
        return True, gear
    return False, gear

def numberator(schematic, numberstoFind):
    number1 = ""
    number1R = schematic[numberstoFind[0][0]][numberstoFind[0][1]:]
    number1L = schematic[numberstoFind[0][0]][:numberstoFind[0][1]]
    number1L.reverse()
    for character in number1R:
        if character.isnumeric():
            number1 = number1 + character
        else:
            break
    for character in number1L:
        if character.isnumeric():
            number1 = character+ number1
        else:
            break
    number2 = ""
    number2R = schematic[numberstoFind[1][0]][numberstoFind[1][1]:]
    number2L = schematic[numberstoFind[1][0]][:numberstoFind[1][1]]
    number2L.reverse()
    for character in number2R:
        if character.isnumeric():
            number2 = number2 + character
        else:
            break
    for character in number2L:
        if character.isnumeric():
            number2 = character+ number2
        else:
            break
    print(f"{number1}*{number2}={int(number1)*int(number2)}")
    gear = int(number1) * int(number2)
    return gear

partList = partfinder(schematic)
gearList = gearfinder(schematic)

print(f"\nPart 1 answer: {sum(partList)}")
print(f"Part 2 answer: {sum(gearList)}")