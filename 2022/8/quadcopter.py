# Challenge input
with open("input.txt") as adventinput:
    treecolumns = adventinput.readlines()

forest = []

# Prepare forest
for column in treecolumns:
    # Add every column to the forest (list of lists), remove the newline characters
    forest.append([*column.strip()])

# Deal with le foresto
treenumber = 1
visibletrees = 0
forestHeight = 99
forestWidth = 99
columnindex = 0

for column in forest:
    # Manually keep an index due to duplicates
    # print(columnindex)
    rowindex = -1
    for row in column:
        rowindex = rowindex + 1
        print(f"\n=== Currently processing tree {treenumber} ===")
        print(f"This tree is in column {columnindex}, row {rowindex}")
        print(f"The current height is: {row}")
        treenumber = treenumber + 1
        treesEast = len(column[rowindex:]) - 1
        treesWest = len(column[:rowindex]) - 1
        treesNorth = columnindex
        treesSouth = forestHeight - columnindex - 1
        ## Basic checks to save cycles
        # Outer trees are always visible - east & west
        if rowindex == 0 or rowindex == 98:
            visibletrees = visibletrees + 1
            print("Tree visible from the outside!")
            continue
        # Outer trees are always visible - north & south
        elif columnindex == 0 or columnindex == 98:
            visibletrees = visibletrees + 1
            print("Tree is visible from the outside!")
            continue

        print(f"East {treesEast}, West {treesWest}, North {treesNorth}, South {treesSouth}")
        
        # Checking East
        print("- Checking if tree is visible from the East:")
        for tree in range(rowindex + 1, treesEast + rowindex + 1, 1):
            print(column[tree], end = "")
            comparetree = column[tree]
            if int(row) <= int(comparetree):
                print(" <- Blocks view\nTree is not visible from the East!")
                isVisible = False
                break
            else:
                isVisible = True
        if isVisible == True:
            print("\nTree is visible from the East!")
            visibletrees = visibletrees + 1
            continue

        # Checking West
        print("\n- Checking if tree is visible from the West:")
        for tree in range(rowindex - 1, rowindex - treesWest, -1):
            print(column[tree], end = "")
            comparetree = column[tree]
            if int(row) <= int(comparetree):
                print(" <- Blocks view\nTree is not visible from the West!")
                isVisible = False
                break
            else:
                isVisible = True
        if isVisible == True:
            print("\nTree is visible from the West!")
            visibletrees = visibletrees + 1
            continue

        # Checking North
        print("\n- Checking if tree is visible from the North:")
        for columnstocheck in range(treesNorth, 0, -1):
            print(forest[columnstocheck][rowindex], end = "")
            comparetree = forest[columnstocheck][rowindex]
            if int(row) <= int(comparetree):
                print(" <- Blocks view\nTree is not visible from the North!")
                isVisible = False
                break
            else:
                isVisible = True
        if isVisible == True:
            print("\nTree is visible from the North!")
            visibletrees = visibletrees + 1
            continue
        
        # Checking South
        print("\n- Checking if tree is visible from the South:")
        for columnstocheck in range(columnindex + 1, forestHeight, 1):
            print(forest[columnstocheck][rowindex], end = "")
            comparetree = forest[columnstocheck][rowindex]
            if int(row) <= int(comparetree):
                print(" <- Blocks view\nTree is not visible from the South!")
                isVisible = False
                break
            else:
                isVisible = True
        if isVisible == True:
            print("\nTree is visible from the South!")
            visibletrees = visibletrees + 1
            continue

    columnindex = columnindex + 1

print(f"\nThere are {visibletrees} visible trees.")
# 1708 = correct
# 1416 = wrong
# 1488 = wrong
# 1202 ?
# 1450 = wrong
# 1447 = wrong