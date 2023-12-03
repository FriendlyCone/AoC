# Challenge input
inputfile = open("input.txt", "r")

# Variables
pair = 0
contained = 0
fullycontained = 0

for line in inputfile:
    pair = pair + 1
    partialmatch = False
    print(f"Processing pair {pair}: ")
    line = line.strip()
    # print(line.split(","))
    grouplist = line.split(",")
    elf1 = grouplist[0].split("-")
    elf1start = int(elf1[0])
    elf1end = int(elf1[1])
    elf2 = grouplist[1].split("-")
    elf2start = int(elf2[0])
    elf2end = int(elf2[1])
    print(f"{elf1start}-{elf1end}")
    print(f"{elf2start}-{elf2end}")
    if elf1start >= elf2start:
        print("Elf 1 start is higher or equal to Elf 2...")
        # Check if partially contained
        if elf1start <= elf2end:
            print("Elf 1 start is lower or equal to Elf 2 end... Partially contained!")
            contained = contained + 1
            partialmatch = True
        # Check if fully contained
        if elf1end <= elf2end:
            print("Elf 1 end is lower or equal to Elf 2 end... Fully contained!")
            fullycontained = fullycontained + 1
            continue
    if elf2start >= elf1start:
        print("Elf 2 start is higher or equal to Elf 1...")
        # Check if partially contained
        print("Elf 2 start is lower or equal to Elf 1 end... Partially contained!")
        if elf2start <= elf1end and not partialmatch:
            contained = contained + 1
        # Check if fully contained
        if elf2end <= elf1end:
            print("Elf 2 end is lower or equal to Elf 1 end... Fully contained!")
            fullycontained = fullycontained + 1
print(f"The range is fully contained by {fullycontained} pairs.")
print(f"The range is partially contained by {contained} pairs.")