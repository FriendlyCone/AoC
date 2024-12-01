import time
startTime = time.time()

leftList = []
rightList = []

# with open("test.txt", "r") as inputfile:
with open("input.txt", "r") as inputfile:
    for line in inputfile:
        left, right = line.split("   ")
        leftList.append(int(left.strip()))
        rightList.append(int(right.strip()))

def part1():
    leftList.sort()
    rightList.sort()
    totalDistance = 0
    for item in range(len(leftList)):
        leftItem = leftList[item]
        rightItem = rightList[item]
        difference = abs(leftItem-rightItem)
        totalDistance = totalDistance + difference
    return totalDistance

def part2():
    similarityScore = 0
    for item in leftList:
        counter = 0
        for comparison in rightList:
            if item == comparison:
                counter = counter + 1
        similarityScore = similarityScore + (item * counter)
    return similarityScore

if __name__ == '__main__':
    isPart2 = False
    part1 = part1()
    part1Runtime = time.time() - startTime

    isPart2 = True
    part2 = part2()
    part2Runtime = time.time() - startTime

    print(f"\nPart 1 answer: {part1}, finished in {part1Runtime}")
    print(f"Part 2 answer: {part2}, finished in {part2Runtime}")