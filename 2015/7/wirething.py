with open("input.txt", "r") as inputfile:
    input = inputfile.read().splitlines()
    input = [command.split(" ") for command in input]

circuitionary = {}
blanksignal16bit = [0]*16
#TEST BIT CAN REMOVE AFTER WORKS
testbit = [0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0]
cmd0, cmd1, cmd2 = 0, 0, 0

def bitconverter(decimal):
    newsignal16bit = [0]*16
    bit = 0
    decimalList = [32768, 16384, 8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    for value in decimalList:
        if decimal >= value:
            newsignal16bit[bit] = 1
            decimal is decimal - value
        bit = bit + 1
    return newsignal16bit

for fullcommand in input:
    print(f"Processing {fullcommand}")
    number = 0
    NOTcommand = ANDcommand = ORcommand = LSHIFTcommand = RSHIFTcommand = False
    for partialcommand in fullcommand:
        # Command options
        # ->
        if "->" in partialcommand:
            continue
        # NOT
        if "NOT" in partialcommand:
            NOTcommand = True
            continue
        # AND
        if "AND" in partialcommand:
            ANDcommand = True
            continue
        # OR
        if "OR" in partialcommand:
            ORcommand = True
            continue
        # LSHIFT
        if "SHIFT" in partialcommand:
            if "LSHIFT" in partialcommand:
                LSHIFTcommand = True
        # RSHIFT
            else:
                RSHIFTcommand = True
            continue
        # ascii
        if partialcommand.isalpha():
            if partialcommand not in circuitionary:
                circuitionary[partialcommand] = blanksignal16bit[:]
        # int
        if partialcommand.isnumeric() and not LSHIFTcommand and not RSHIFTcommand:
            partialcommand = bitconverter(int(partialcommand))
        # int or ascii
        globals()["cmd" + str(number)] = partialcommand
        number = number + 1        

# Process different commands
#Entries look like:
    index = 0

# NOT cv -> cw
    if NOTcommand:
        # Bitflipping time
        print("NOT command found.")
        if not type(cmd0) is list:
            NOTbit = circuitionary[cmd0]
        else:
            NOTbit = cmd0
        if not type(cmd1) is list:
            TARbit = circuitionary[cmd1]
        else:
            TARbit = cmd1
        print(f"{NOTbit} = {cmd0}")
        print(f"{TARbit} = {cmd1}")
        for bit in TARbit:
            if bit == NOTbit[index]:
                if bit == 0:
                    TARbit[index] = 1
                else:
                    TARbit[index] = 0
            index = index + 1
        print(f"{TARbit} = the result after the NOT operation")
        circuitionary[cmd1] = TARbit
        continue

# as AND bd -> bf
# 1 AND cc -> cd
    if ANDcommand:
        print("AND command found.")
        if not type(cmd0) is list:
            ANDbit = circuitionary[cmd0]
        else:
            ANDbit = cmd0
        if not type(cmd1) is list:
            TARbit = circuitionary[cmd1]
        else:
            TARbit = cmd1
        DSTbit = circuitionary[cmd2]
        print(f"{ANDbit} = {cmd0}")
        print(f"{TARbit} = {cmd1}")
        for bit in TARbit:
            if bit == ANDbit[index] and bit != 0:
                DSTbit[index] = 1
            else:
                DSTbit[index] = 0
            index = index + 1
        print(f"{DSTbit} = the result after the AND operation")
        circuitionary[cmd2] = DSTbit
        continue

# ki OR kj -> kk
    if ORcommand:
        print("OR command found.")
        if not type(cmd0) is list:
            ORbit = circuitionary[cmd0]
        else:
            ORbit = cmd0
        if not type(cmd1) is list:
            TARbit = circuitionary[cmd1]
        else:
            TARbit = cmd1
        DSTbit = circuitionary[cmd2]
        print(f"{ORbit} = {cmd0}")
        print(f"{TARbit} = {cmd1}")
        for bit in TARbit:
            if bit == 1:
                DSTbit[index] = 1
            elif TARbit[index] == 1:
                DSTbit[index] = 1
            else:
                DSTbit[index] = 0
            index = index + 1
        print(f"{DSTbit} = the result after the OR operation")
        circuitionary[cmd2] = DSTbit
        continue
        
# hb LSHIFT 1 -> hv
    if LSHIFTcommand:
        print("LSHIFT command found.")
        SRCbit = circuitionary[cmd0]
        shiftnum = int(cmd1)
        print(f"{SRCbit} = {cmd0}")
        print(f"Shift by {shiftnum}")
        while shiftnum > 0:
            firstSRCbit = SRCbit[0:1]
            restSRCbit = SRCbit[1:]
            SRCbit = restSRCbit + firstSRCbit
            shiftnum = shiftnum - 1
            print(SRCbit)
        print(f"{SRCbit} = the result after the LSHIFT operation")
        circuitionary[cmd2] = SRCbit
        continue

# he RSHIFT 3 -> hg
    if RSHIFTcommand:
        print("RSHIFT command found.")
        SRCbit = circuitionary[cmd0]
        shiftnum = int(cmd1)
        print(f"{SRCbit} = {cmd0}")
        print(f"Shift by {shiftnum}")
        while shiftnum > 0:
            lastSRCbit = SRCbit[-1:]
            restSRCbit = SRCbit[:-1]
            SRCbit = lastSRCbit + restSRCbit
            shiftnum = shiftnum - 1
            print(SRCbit)
        print(f"{SRCbit} = the result after the RSHIFT operation")
        circuitionary[cmd2] = SRCbit
        continue

# lx -> a
# 14146 -> b
    print("Bit set command found.")
    print(cmd0)
    if not type(cmd0) is list:
        cmd0 = circuitionary[cmd0]
    print(cmd1)
    circuitionary[cmd1] = cmd0
    
print(circuitionary)
print(circuitionary['a'])