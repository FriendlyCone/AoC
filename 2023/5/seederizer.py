import concurrent.futures
import time
startTime = time.time()

with open("input.txt", "r") as inputfile:

    # Define required lists
    seed_soilList, soil_fertilizerList, fertilizer_waterList, water_lightList, light_tempList, temp_humidList, humid_locList = [], [], [], [], [], [], []
    recordTriggers = ["seed-to-soil map", "soil-to-fertilizer map", "fertilizer-to-water map", "water-to-light map", "light-to-temperature map", "temperature-to-humidity map", "humidity-to-location map"]

    # Define recording triggers
    seedsoilrecord = False
    soiltofertilizerrecord = False
    fertilizertowaterrecord = False
    watertolightrecord = False
    lighttotemperaturerecord = False
    temperaturetohumidityrecord = False
    humiditytolocationrecord = False

    for line in inputfile:
    # Create seed list:
        if "seeds:" in line:
            x, seedList = line.split(":")
            seedList = seedList.split()
    # Check if recording end
        if line == "\n":
            seedsoilrecord = False
            soiltofertilizerrecord = False
            fertilizertowaterrecord = False
            watertolightrecord = False
            lighttotemperaturerecord = False
            temperaturetohumidityrecord = False
            humiditytolocationrecord = False

    # Create maps
        if seedsoilrecord:
            seed_soilList.append(line.split())
        elif soiltofertilizerrecord:
            soil_fertilizerList.append(line.split())
        elif fertilizertowaterrecord:
            fertilizer_waterList.append(line.split())
        elif watertolightrecord:
            water_lightList.append(line.split())
        elif lighttotemperaturerecord:
            light_tempList.append(line.split())
        elif temperaturetohumidityrecord:
            temp_humidList.append(line.split())
        elif humiditytolocationrecord:
            humid_locList.append(line.split())
            
    # Check recording triggers
        if "seed-to-soil map" in line:
            seedsoilrecord = True
        elif "soil-to-fertilizer map" in line:
            soiltofertilizerrecord = True
        elif "fertilizer-to-water map" in line:
            fertilizertowaterrecord = True
        elif "water-to-light map" in line:
            watertolightrecord = True
        elif "light-to-temperature map" in line:
            lighttotemperaturerecord = True
        elif "temperature-to-humidity map" in line:
            temperaturetohumidityrecord = True
        elif "humidity-to-location map" in line:
            humiditytolocationrecord = True

# Prepare input so I don't have to copy lots of code
def inputerizer(seedsList, isPart2):
    # Create new list with the part 2 pairs. Also convert the Length modifier to just be the end of the range
    rangeList = []
    if isPart2:
        pairList = []
        isStart = True
        isLength = False
        for seed in seedsList:
            if isStart:
                pairEntry = []
                startRange = int(seed)
                pairEntry.append(startRange)
                isStart, isLength = False, True
            elif isLength:
                endRange = startRange + int(seed) - 1
                pairEntry.append(endRange)
                pairList.append(pairEntry)
                isStart, isLength = True, False        
                rangeList.append([pairEntry[0], pairEntry[1]])
    else:
        for seed in seedsList:
            rangeList.append([int(seed), int(seed)])

    resultList = []
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for seed, output in zip(rangeList, executor.map(multithreaderizer, rangeList)):
            resultList.append(output)
    lowestLoc = min(resultList)
    return lowestLoc

# Multithreading time bitches
def multithreaderizer(inputRange):
    output = seederizer(inputRange)
    return output

# Go over all mappings, set up part 2 if needed.
def seederizer(inputRange):
    input = [inputRange]
    input = almanaccheck(input, seed_soilList)
    input = almanaccheck(input, soil_fertilizerList)
    input = almanaccheck(input, fertilizer_waterList)
    input = almanaccheck(input, water_lightList)
    input = almanaccheck(input, light_tempList)
    input = almanaccheck(input, temp_humidList)
    input = almanaccheck(input, humid_locList)
    output = answerinator(input)
    return output

def answerinator(inputList):
    answerList = []
    for locRange in inputList:
        answerList.append(locRange[0])
    return min(answerList)

# Process fed mapping
def almanaccheck(input, map):
    processingRange = []
    output = []
    sliceList = []
    for seedrange in input:
        for row in map:
            dstrangestart = int(row[0])
            srcrangestart = int(row[1])
            rangelength = int(row[2]) - 1
            comparison = [srcrangestart, srcrangestart+rangelength]
            diff = dstrangestart - srcrangestart
            # Check if whole range fits
            if seedrange[0] >= comparison[0] and seedrange[-1] <= comparison[-1]:
                processingRange = [seedrange[0]+diff, seedrange[-1]+diff]
                output.append(processingRange)
                break
            # Check if fully not contained
            elif seedrange[-1] < comparison[0] or seedrange[0] > comparison[-1]:
                # Check if last mapping to be checked
                if map[-1] == row:
                    processingRange = seedrange
                    output.append(processingRange)
            # Check partial match left
            elif seedrange[-1] < comparison[-1] and not seedrange[0] > comparison[0]:
                # Contained
                containedRange = [comparison[0]+diff, seedrange[-1]+diff]
                output.append(containedRange)
                # Not contained
                partialRange = [seedrange[0], comparison[0]-1]
                sliceList.append(partialRange)
                break
            # Check partial match right
            elif seedrange[0] > comparison[0] and not seedrange[-1] < comparison[-1]:
                containedRange = [seedrange[0]+diff, comparison[-1]+diff]
                output.append(containedRange)
                # Not contained
                partialRange = [comparison[-1]+1, seedrange[-1]]
                sliceList.append(partialRange)
                break
    if sliceList:
        extraOutput = almanaccheck(sliceList, map)
        output = output + extraOutput
    dedupList = []
    [dedupList.append(x) for x in output if x not in dedupList]
    output = dedupList
    return output

# Get answers and time it for funsies
if __name__ == '__main__':
    part1 = inputerizer(seedList, False)
    part1Runtime = time.time() - startTime
    part2 = inputerizer(seedList, True)
    part2Runtime = time.time() - startTime
    print(f"\nPart 1 answer: {part1}, finished in {part1Runtime}")
    print(f"Part 2 answer: {part2}, finished in {part2Runtime}\n")