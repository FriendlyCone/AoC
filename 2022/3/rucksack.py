# Imports
import string

# Challenge input
inputfile = open("input.txt", "r")

# Variables
numrucksack = 0
duplicateitem = ""
characterset = string.ascii_lowercase + string.ascii_uppercase
charactersetlist = [*characterset]
value = 0
valuedict = {}
totalduplicatevalues = 0

# Item value builder because lazy af
for character in charactersetlist:
    value = value + 1
    valuedict.update({character: value})

# Rucksack checker
for line in inputfile:
    #Increase rucksack ID by 1 and show user
    numrucksack = numrucksack + 1
    print(f"\n==========Rucksack number #{numrucksack}==========")
    # Split line in 2 equal parts
    print(f"{len(line.strip())} characters in {line.strip()}")
    comp1 = line[:len(line)//2]
    comp2 = line[len(line)//2:]
    print(f"Compartment 1: {comp1}")
    print(f"Compartment 2: {comp2}".strip())
    # Get all unique characters in Compartment 1
    uniquecomp1 = "".join(set(comp1))
    uniquelist = [*uniquecomp1]
    print(f'Unique characters in first half: {uniquecomp1}')
    # Check which characters are duplicate
    print("Checking for duplicate characters: ", end = "")
    for character in uniquelist:
        print(f'{comp2.count(character)} ', end = '')
        if comp2.count(character) > 0:
            duplicateitem = character
    print(f"\nThe duplicate item is: {duplicateitem}")
    duplicateitemvalue = valuedict.get(duplicateitem)
    print(f"The value of the item is: {duplicateitemvalue}")
    totalduplicatevalues = totalduplicatevalues + duplicateitemvalue
    print (f"The current total duplicate value is {totalduplicatevalues}")