import time
startTime = time.time()

cardValues =[
    ['2', 1],
    ['3', 2],
    ['4', 3],
    ['5', 4],
    ['6', 5],
    ['7', 6],
    ['8', 7],
    ['9', 8],
    ['T', 9],
    ['J', 10],
    ['Q', 11],
    ['K', 12],
    ['A', 13]
]
gameList = []

with open("test.txt", "r") as inputfile:
# with open("input.txt", "r") as inputfile:
    for line in inputfile:
        # Split into hand + score
        newhandEntry = []
        handEntry, scoreEntry = line.split()
        handEntry = [*handEntry]
        # Easier to turn hands into numbers
        for entry in handEntry:
            for cardValue in cardValues:
                if entry == cardValue[0]:
                    newhandEntry.append(cardValue[1])
        handEntry = newhandEntry
        gameList.append([handEntry, int(scoreEntry)])

# There is 7 hand types, need to score it based on hand type, and if same type check more valuable
def rankinator(currentgame, rankList):
    cardRange = range(1, 14)
    currentHand = currentgame[0]
    currentType = 0
    typeCheck = []
    pairOne = 0
    pairTwo = 0
    print(currentgame)
    # Find type of current hand first
    for card in cardRange:
        cardAmount = currentHand.count(card)
        print(f"Checking for {card}, we found: {cardAmount}")
        if cardAmount == 2 and not pairOne:
            pairOne = card
        elif cardAmount == 2 and pairOne:
            pairTwo = card
    print(pairOne)
    print(pairTwo)

def initial(gameList):
    rankedList = []
    # Gotta rank them games
    for game in gameList:
        if not rankedList:
            rankedList.append(game)
        else:
            rankinator(game, rankedList)
                    


if __name__ == '__main__':
    part1 = initial(gameList)
    part1Runtime = time.time() - startTime

    part2 = initial(gameList)
    part2Runtime = time.time() - startTime

    print(f"\nPart 1 answer: {part1}, finished in {part1Runtime}")
    print(f"Part 2 answer: {part2}, finished in {part2Runtime}")