with open("input.txt", "r") as inputfile:
    rawcalculations = []
    for line in inputfile:
        rawcalculations.append(line.strip())

def magicalextractinator(inputline, parttwo):
    LR_INT, RL_INT = 0, 0
    print(inputline)
    if parttwo:
        inputline = inputline.replace("one", "one1one")
        inputline = inputline.replace("two", "two2two")
        inputline = inputline.replace("three", "three3three")
        inputline = inputline.replace("four", "four4four")
        inputline = inputline.replace("five", "five5five")
        inputline = inputline.replace("six", "six6six")
        inputline = inputline.replace("seven", "seven7seven")
        inputline = inputline.replace("eight", "eight8eight")
        inputline = inputline.replace("nine", "nine9nine")
        print(inputline)
    currentitem = [*inputline]
    print(f"\nCurrently processing: {currentitem}")
    for character in currentitem:
        if character.isnumeric():
            print(f"Found left-to-right int! - {character}")
            LR_INT = character
            break
    currentitem.reverse()
    for character in currentitem:
        if character.isnumeric():
            print(f"Found right-to-left int! - {character}")
            RL_INT = character
            break
    calculation = str(LR_INT) + str(RL_INT)
    print(calculation)
    return calculation

# Part 1
calibrationvalues = []
for value in rawcalculations:
    calcvalue = magicalextractinator(value, False)
    calibrationvalues.append(calcvalue)

# What is the sum of all the values?
total1 = 0
for value in calibrationvalues:
    value = int(value)
    total1 = total1 + value

# Part 2
calibrationvalues = []
for value in rawcalculations:
    calcvalue = magicalextractinator(value, True)
    calibrationvalues.append(calcvalue)

# What is the sum of all the values?
total2 = 0
for value in calibrationvalues:
    value = int(value)
    total2 = total2 + value

print(f"\nPart one total is {total1}")
print(f"Part two total is {total2}")

# 53429 - too low?