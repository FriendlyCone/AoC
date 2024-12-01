import time
startTime = time.time()

rawinitList = []
initList = []

# with open("test.txt", "r") as inputfile:
with open("input.txt", "r") as inputfile:
    for line in inputfile:
        rawinitList.append(line.split(","))
        for entry in rawinitList:
            initList.append(*entry)
    # initList = [*initString for initString in initList]
    print(initList)

def initial():
    for initString in initList:
        currentValue = 0
        for character in initString:
            currentValue = currentValue + ord(character)
            currentValue = currentValue * 17
            currentValue = currentValue / 256


if __name__ == '__main__':
    isPart2 = False
    part1 = initial()
    part1Runtime = time.time() - startTime

    isPart2 = True
    part2 = initial()
    part2Runtime = time.time() - startTime

    print(f"\nPart 1 answer: {part1}, finished in {part1Runtime}")
    print(f"Part 2 answer: {part2}, finished in {part2Runtime}")