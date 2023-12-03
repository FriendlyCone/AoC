# Imports
import string

# Challenge input
inputfile = open("input.txt", "r")

# Variables
rucksack = 0
rucksacklist = []
duplicateitem = ""
characterset = string.ascii_lowercase + string.ascii_uppercase
charactersetlist = [*characterset]
value = 0
valuedict = {}
totalduplicatevalues = 0
group = 0

# Item value builder because lazy af
for character in charactersetlist:
    value = value + 1
    valuedict.update({character: value})

# Rucksack checker
for line in inputfile:
    # Make groups of 3
    rucksack = rucksack + 1
    rucksacklist.append(line.strip())
    if rucksack == 3:
        group = group + 1
        rucksack = 0
        print(f"Group {group}")
        sack1, sack2, sack3 = rucksacklist[0], rucksacklist[1], rucksacklist[2]
        print(f"Sack 1 contains: {sack1}")
        print(f"Sack 2 contains: {sack2}")
        print(f"Sack 3 contains: {sack3}")
        rucksacklist = []
        # Get all unique characters in Sack 1
        uniquesack1 = "".join(set(sack1))
        uniquelist = [*uniquesack1]
        print(f'Unique characters in first sack: {uniquesack1}')
        # Check character matches vs Sack 2
        for character in uniquelist:
            if sack2.count(character) > 0:
                print(f"{character} in Sack 2, ", end="")
                # Check character matches vs Sack 3
                if sack3.count(character) > 0:
                    print(f"in Sack 3, Match found! - {character}")
                    duplicateitem = character
                    duplicateitemvalue = valuedict.get(duplicateitem)
                    print(f"The value of the item is: {duplicateitemvalue}")
                    totalduplicatevalues = totalduplicatevalues + duplicateitemvalue
                    print (f"The current total duplicate value is {totalduplicatevalues}")
                    break
                else:
                    print(f"not in Sack 3.")
            elif sack2.count(character) == 0:
                print(f"{character} not in Sack 2.")