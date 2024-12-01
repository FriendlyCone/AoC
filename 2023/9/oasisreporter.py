import time
startTime = time.time()
sensorDataList = []

# with open("test.txt", "r") as inputfile:
with open("input.txt", "r") as inputfile:
    for line in inputfile:
        sensorData = line.split()
        sensorData = [int(Data) for Data in sensorData]
        sensorDataList.append(sensorData)

def oasisExtrapolator(sensorData):
    zeroSequenceFound = False
    extrapolationChain = []
    newsensorData = sensorData.copy()
    extrapolationChain.append(newsensorData)
    while not zeroSequenceFound:
        newextrapolationChainEntry = []
        extrapolation = extrapolationChain[-1]
        extrapolationSize = range(0, len(extrapolation)-1)
        # Comparison time
        for index in extrapolationSize:
            compareLeft, compareRight = extrapolation[index], extrapolation[index+1]
            difference = compareRight - compareLeft
            newextrapolationChainEntry.append(difference)
        extrapolationChain.append(newextrapolationChainEntry)
        if newextrapolationChainEntry.count(0) == len(newextrapolationChainEntry):
            zeroSequenceFound = True
    return extrapolationChain

def oasisPredictinator(extrapolationChain):
    predictedChain = []
    chainLength = range(0, len(extrapolationChain)-1)
    for chain in extrapolationChain:
        if isPart2:
            chain.reverse()
        chain.append(0)
        chain.reverse()
    extrapolationChain.reverse()
    for index in chainLength:
        currentData = extrapolationChain[index]
        nextData = extrapolationChain[index+1]
        currentFirst = currentData[0]
        nextSecond = nextData[1]
        if isPart2:
            nextEntry = nextSecond - currentFirst
        else:
            nextEntry = currentFirst + nextSecond
        nextData[0] = nextEntry
    output = nextEntry
    return output

def answerinator(predictionList):
    answer = sum(predictionList)
    return answer

def initial(sensorDataList):
    # We need to create a new list of lists per entry in sensorDataList to extrapolate
    predictionList = []
    extrapolationChain = []
    for sensorData in sensorDataList:
        extrapolationChain = oasisExtrapolator(sensorData)
        output = oasisPredictinator(extrapolationChain)
        predictionList.append(output)
    answer = answerinator(predictionList)
    return answer

if __name__ == '__main__':
    isPart2 = False
    print(sensorDataList)
    part1 = initial(sensorDataList)
    part1Runtime = time.time() - startTime

    isPart2 = True
    print(sensorDataList)
    part2 = initial(sensorDataList)
    part2Runtime = time.time() - startTime

    print(f"\nPart 1 answer: {part1}, finished in {part1Runtime}")
    print(f"Part 2 answer: {part2}, finished in {part2Runtime}")