import time
startTime = time.time()

instructionList = []
networkNodes = {}

# with open("test.txt", "r") as inputfile:
with open("input.txt", "r") as inputfile:
    for line in inputfile:
        # We take the direction as a dictionary
        if instructionList and not line == "\n":
            # First we clean
            nodeKey, instructionRaw = line.split("=")
            nodeKey, instructionRaw = nodeKey.strip(), instructionRaw.strip()
            instructionRaw = instructionRaw.replace("(", "")
            instructionRaw = instructionRaw.replace(")", "")
            instructionL, instructionR = instructionRaw.split(",")
            instructionL, instructionR = instructionL.strip(), instructionR.strip()
            nodeValue = [instructionL, instructionR]
            # Then we write
            networkNodes.update({nodeKey: nodeValue})
        # We take the instructions as a list
        elif not instructionList:
            instructionList = [*line.strip()]

def navigator(activeNode, stepCounter):
    for instruction in instructionList:
        stepCounter = stepCounter + 1
        activeValue = networkNodes.get(activeNode)
        if instruction == "L":
            activeNode = activeValue[0]
        else:
            activeNode = activeValue[1]
    return activeNode, stepCounter

def loopfinder(activeNode, stepCounter, hitListValues):
    for instruction in instructionList:
        stepCounter = stepCounter + 1
        if isPart2 and activeNode.endswith("Z"):
            print(activeNode)
            hitListValues.append(stepCounter)
        activeValue = networkNodes.get(activeNode)
        if instruction == "L":
            activeNode = activeValue[0]
        else:
            activeNode = activeValue[1]
    return activeNode, stepCounter, hitListValues

def initial():
    activeNode = "AAA"
    stepCounter = 0
    if isPart2:
        # First we have to find all the nodes that end in A
        startNodes = []
        for key in networkNodes.keys():
            if key.endswith("A"):
                startNodes.append(key)
        pathstoFollow = len(startNodes)
        stepSaver = [0]*pathstoFollow
        hitList = [[]]*pathstoFollow
        print(startNodes)
        print(stepSaver)
        print(hitList)
        foundAllMatches = False
        # Then we have to find all the places where we match the lowest
        # THIS CURRENTLY DOESN'T WORK
        while not foundAllMatches:
            for activeNode in startNodes:
                print(f"We are at checking {activeNode}")
                currentIndex = startNodes.index(activeNode)
                stepCounter = stepSaver[currentIndex]
                currentHitList = hitList[currentIndex]
                activeNode, stepCounter, hitListValues = loopfinder(activeNode, stepCounter, currentHitList)
                # Update the start node for next cycle
                startNodes[currentIndex] = activeNode
                # Update the start count for next cycle
                stepSaver[currentIndex] = stepCounter
                hitList[currentIndex] = hitListValues
                print(currentIndex)
                print(stepSaver)
                print(startNodes)
                print(hitList)
            # Check if a stepcount exists 6 times
            hitCount = 0
            for entry in hitList[0]:
                for list in hitList:
                    if entry in list:
                        hitCount = hitCount + 1
                        if hitCount == 6:
                            foundAllMatches = True
            # break
        
    else:
        while not activeNode == "ZZZ":
            activeNode, stepCounter = navigator(activeNode, stepCounter)
    answer = stepCounter
    return answer


if __name__ == '__main__':
    isPart2 = False
    part1 = initial()
    part1Runtime = time.time() - startTime

    isPart2 = True
    part2 = initial()
    part2Runtime = time.time() - startTime

    print(f"\nPart 1 answer: {part1}, finished in {part1Runtime}")
    print(f"Part 2 answer: {part2}, finished in {part2Runtime}")
    
# 15517 is too low
# 93365 is wrong
# 12624