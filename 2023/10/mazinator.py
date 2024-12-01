import time
startTime = time.time()

with open("input.txt", "r") as inputfile:
    grid = []
    for line in inputfile:
        column = [*line.strip()]
        grid.append(column)


compassDirections = [
    "|", # N-S Pipe
    "-", # E-W Pipe
    "L", # N-E Pipe
    "J", # N-W Pipe
    "7", # S-W Pipe
    "F", # S-E Pipe
    "."  # No Pipe
    ]

def initial(grid):
    partList = []
    numberlength = 0
    number = ""
    coordX = 0
    coordY = 0
    processing = False
    # Process Grid
    for x in grid:
        for y in x:
            # Find Start
            if y == "S":
                numberlength = numberlength + 1
                number = number + y
                if not processing:
                    processing = True
                    digitcoordYstart = coordY
            if numberlength > 0 and not y.isnumeric():
                print(f"\nFound whole number {number}, it is {numberlength} digits.")
                print(f"The X is {coordX}, the Y range is {digitcoordYstart} to {digitcoordYstart+numberlength-1}")
                if checknextdirection(grid, coordX, digitcoordYstart, numberlength):
                    partList.append(int(number))
                numberlength = 0
                number = ""
                processing = False
            coordY = coordY + 1
        coordY = 0
        coordX = coordX + 1
    return partList

def checknextdirection(grid, coordX, startY, numberlength):
    for x in range(-1, 2, 1):
        if coordX+x >= 0 and coordX+x <= len(grid)-1:
            pass
        else:
            continue
        for y in range(startY-1, startY+numberlength+1, 1):
            if y >= 0 and y <= len(grid[0])-1:
                print(f"{grid[coordX+x][y]}", end="")
                pass
            else:
                continue
            if grid[coordX+x][y] in specialList:
                print(f"\nConfirmed it is a part: {grid[coordX+x][y]}")
                return True
        print("\n", end="")
    return False


if __name__ == '__main__':
    isPart2 = False
    part1 = initial(grid)
    part1Runtime = time.time() - startTime

    isPart2 = True
    # part2 = initial()
    # part2Runtime = time.time() - startTime

    print(f"\nPart 1 answer: {part1}, finished in {part1Runtime}")
    # print(f"Part 2 answer: {part2}, finished in {part2Runtime}")






# gearList = gearfinder(grid)

# def numberator(schematic, numberstoFind):
#     number1 = ""
#     number1R = schematic[numberstoFind[0][0]][numberstoFind[0][1]:]
#     number1L = schematic[numberstoFind[0][0]][:numberstoFind[0][1]]
#     number1L.reverse()
#     for character in number1R:
#         if character.isnumeric():
#             number1 = number1 + character
#         else:
#             break
#     for character in number1L:
#         if character.isnumeric():
#             number1 = character+ number1
#         else:
#             break
#     number2 = ""
#     number2R = schematic[numberstoFind[1][0]][numberstoFind[1][1]:]
#     number2L = schematic[numberstoFind[1][0]][:numberstoFind[1][1]]
#     number2L.reverse()
#     for character in number2R:
#         if character.isnumeric():
#             number2 = number2 + character
#         else:
#             break
#     for character in number2L:
#         if character.isnumeric():
#             number2 = character+ number2
#         else:
#             break
#     print(f"{number1}*{number2}={int(number1)*int(number2)}")
#     gear = int(number1) * int(number2)
#     return gear

# def checkifgear(schematic, coordX, coordY):
#     gear = 0
#     foundDigits = 0
#     numberstoFind = []
#     for x in range(-1, 2, 1):
#         gap = True
#         if coordX+x >= 0 and coordX+x <= len(schematic)-1:
#             pass
#         else:
#             continue
#         for y in range(coordY-1, coordY+2, 1):
#             if y >= 0 and y <= len(schematic[0])-1:
#                 print(f"{schematic[coordX+x][y]}", end="")
#                 pass
#             else:
#                 continue
#             if schematic[coordX+x][y].isnumeric() and gap:
#                 numberstoFind.append([coordX+x, y])
#                 foundDigits = foundDigits + 1
#                 gap = False
#             elif not schematic[coordX+x][y].isnumeric():
#                 gap = True
#         print("\n", end="")
#     if foundDigits == 2:
#         print("Found exactly 2 attached numbers.")
#         gear = numberator(schematic, numberstoFind)
#         return True, gear
#     return False, gear
