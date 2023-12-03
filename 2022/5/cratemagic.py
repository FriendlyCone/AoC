# Challenge input
inputfile = open("input.txt", "r").read()

# Variables
startpositions, moveset = inputfile.split("\n\n")
startpositions, moveset = startpositions.splitlines(), moveset.splitlines()
stacks = {}
cratemover = input("What CrateMover is in use?\n1 = CrateMover 9000\n2 = CrateMover 9001\nChoice: ")

# Initial layout:                     Column
#         [Q] [B]         [H]         = 0
#     [F] [W] [D] [Q]     [S]         = 1
#     [D] [C] [N] [S] [G] [F]         = 2
#     [R] [D] [L] [C] [N] [Q]     [R] = 3
# [V] [W] [L] [M] [P] [S] [M]     [M] = 4
# [J] [B] [F] [P] [B] [B] [P] [F] [F] = 5
# [B] [V] [G] [J] [N] [D] [B] [L] [V] = 6
# [D] [P] [R] [W] [H] [R] [Z] [W] [S] = 7
#  0   1   2   3   4   5   6   7   8  = Python
#  1   2   3   4   5   6   7   8   9  = Human

# Create inital layout
# Iterate over every column, removing -1 to start at 0, going in reverse
for column in range(len(startpositions)-2,-1,-1):

    # Iterate over every row, starting at 1 to remove the bracket, moving in steps of 4 to go to the next row
    for crate in range(1,len(startpositions[0]), 4):

        # Set variables for the crate letter, row number for easier reading
        cratename, row = startpositions[column][crate], crate//4

        # Check if there is a crate there (uppercase letter vs space)
        print(f"Currently checking row {row}, column {column}:")
        if cratename.isupper():

            # Create dictionary with crates per row for easy modification
            stacks.setdefault(row, []).append(cratename)
            print(f"Contains: {cratename}")
        else:
            print("Contains: Nothing")

print("Current contents:")
for row in stacks:
    print(f"Row {row+1} contains {''.join(stacks[row])}")

# Iterate over all the moves and execute them
for move in moveset:
    x,amount,x,source,x,destination = move.split()

    # Account for list starting at 0, cast to int
    amount = int(amount)
    source,destination = int(source)-1, int(destination)-1

    # Check the length of the stack for the split
    stacklength = len(stacks[source])

    # Grab items with crane
    craneinventory = stacks[source][stacklength-amount:]

    # Reverse the list because items are moved one by one
    if cratemover == "2":
        pass
    else:
        craneinventory.reverse()
    print(f"Currently held by crane: {''.join(craneinventory)}")

    # Removing grabbed crates from source row
    stack = stacks[source][:stacklength-amount]
    stacks.update({source: stack})

    # Deposit crates into destination row
    stack = stacks[destination] + craneinventory
    stacks.update({destination: stack})

print("\nUpdated contents:")
for row in stacks:
    print(f"Row {row+1} contains {''.join(stacks[row])}")

print("Final top order:")
for row in stacks:
    print(f"{''.join(stacks[row][-1])}", end = "")