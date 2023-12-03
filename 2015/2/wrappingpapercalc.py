allBoxes = []
paperneeded, ribbonneeded = 0, 0

with open("input.txt", "r") as inputfile:
    for line in inputfile:
        singleBox = (line.strip().split("x"))
        # Turn entries into integers
        singleBox = [int(dimension) for dimension in singleBox]
        allBoxes.append(singleBox)

# dimensions provided in l, w, h format
# 2*l*w
# 2*w*h
# 2*h*l

for box in allBoxes:
    # Define box sides for easy readability
    l, w, h = box[0], box[1], box[2]
    # Calculate paper required per sides * 2, get total after
    calc1 = 2 * l * w
    calc2 = 2 * w * h
    calc3 = 2 * h * l
    total = calc1 + calc2 + calc3
    
    # Calculate smallest side for slack
    slack = min(l*w, w*h, h*l)

    #Total with slack
    totalslack = total + slack
    # Print per box because I just love output
    print(f"Box: {l}, {w}, {h}")
    print(f"Wrapping Paper: {calc1} + {calc2} + {calc3} = {total} feet, add {slack} feet slack to get {totalslack} feet of wrapping paper.")

    #Keep track of all paper required
    paperneeded = paperneeded + totalslack

    # Part 2, feet of ribbon needed
    ribbon1 = sorted(box)[0] * 2
    ribbon2 = sorted(box)[1] * 2
    ribbontotal = ribbon1 + ribbon2
    bow = l * w * h
    ribbonbow = ribbontotal + bow
    ribbonneeded = ribbonneeded + ribbonbow
    print(f"Ribbon & Bow: {ribbon1} + {ribbon2} = {ribbontotal}, add {bow} feet for the bow to get {ribbonbow}")
print(f"We need {paperneeded} feet of wrapping paper.")
print(f"We need {ribbonneeded} feet of ribbon.")