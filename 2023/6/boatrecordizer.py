import time
startTime = time.time()

# with open("test.txt", "r") as inputfile:
with open("input.txt", "r") as inputfile:
    # Get times
    for line in inputfile:
        if "Time:" in line:
            x, y = line.split(":")
            timeList = y.split()
            timeListPart2 = timeList.copy()
            timeListPart2 = ["".join(timeListPart2)]
            timeListPart2 = [int(time) for time in timeListPart2]
            timeList = [int(time) for time in timeList]
        if "Distance:" in line:
            x, y = line.split(":")
            distanceList = y.split()
            distanceListPart2 = distanceList.copy()
            distanceListPart2 = ["".join(distanceListPart2)]
            distanceListPart2 = [int(time) for time in distanceListPart2]
            distanceList = [int(distance) for distance in distanceList]

# Make pairs of the races
def racelisterizer(timeList, distanceList):
    raceList = []
    race = []
    for races in range(0, len(timeList)):
        race = [timeList[races], distanceList[races]]
        raceList.append(race)
    answer = matherizer(raceList)
    return answer

# Calculate the wins
def matherizer(raceList):
    winnerList = []
    answer = 1
    for race in raceList:
        winner = 0
        raceTime = race[0]
        raceTimeRange = range(0, raceTime)
        raceDistanceRecord = race[1]
        # print(f"\n=== Calculating race with a duration of {raceTime} and a record of {raceDistanceRecord} ===")
        for ms in raceTimeRange:
            speed = ms
            remainingime = raceTime - ms
            distance = ms * remainingime
            # print(f"Holding for {ms}, our speed is {speed}. The remaining time we have is {remainingime}. The distance we go is {distance}.", end="")
            if distance > raceDistanceRecord:
                # print(" We win!")
                winner = winner + 1
            # else:
                # print(" We lose!")
        winnerList.append(winner)
    for wins in winnerList:
        answer = answer * wins
    return answer

part1 = racelisterizer(timeList, distanceList)
part1Runtime = time.time() - startTime

part2 = racelisterizer(timeListPart2, distanceListPart2)
part2Runtime = time.time() - startTime

print(f"\nPart 1 answer: {part1}, finished in {part1Runtime}")
print(f"Part 2 answer: {part2}, finished in {part2Runtime}")