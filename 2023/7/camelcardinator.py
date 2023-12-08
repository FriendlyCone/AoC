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

# with open("test.txt", "r") as inputfile:
with open("input.txt", "r") as inputfile:
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
def rankinator(checkingHand, rankList):
    currentcheckingHand = checkingHand[0]
    hadTieBreak = False
    rankList.reverse()
    newrankList = rankList.copy()
    # Find type of current hand first
    currentHandType = handChecker(currentcheckingHand)
    # Check ranking against other hands
    # Go over the hands in the current ranking
    for rankedHand in rankList:
        currentrankedHand = rankedHand[0]
        rankedHandType = handChecker(currentrankedHand)
        # Rank: Higher is better
        # Rank default: 1, 2, 3, 4
        # Rank reverse: 4, 3, 2, 1
        # If we win, place it on the loser's index
        if currentHandType > rankedHandType and not hadTieBreak:
            newPosition = newrankList.index(rankedHand)
            newrankList.insert(newPosition, checkingHand)
            break
        # If we lose, do nothing unless its the last hand, then put it at the end.
        elif currentHandType < rankedHandType and not hadTieBreak:
            if rankedHand == rankList[-1]:
                newrankList.append(checkingHand)
        # If the hand type is the same, put it in the tiebreaker.
        elif currentHandType == rankedHandType:
            currenthandWins = tieBreak(currentcheckingHand, currentrankedHand)
            # If we win the tiebreaker, put it in the loser's index.
            if currenthandWins:
                newPosition = newrankList.index(rankedHand)
                newrankList.insert(newPosition, checkingHand)
                hadTieBreak = False
                break
            else:
                newPosition = newrankList.index(rankedHand) + 1
                hadTieBreak = True
        elif hadTieBreak:
            newrankList.insert(newPosition, checkingHand)
            hadTieBreak = False
            break
    if hadTieBreak:
        newrankList.insert(newPosition, checkingHand)
        hadTieBreak = False
    # print(newrankList)
    newrankList.reverse()
    return newrankList

# Used for breaking ties
def tieBreak(firstHand, secondHand):
    # For Part 2 Joker is weaker, have to change value to 0
    for firstCard, secondCard in zip(firstHand, secondHand):
        if isPart2:
            if firstCard == 10:
                firstCard = 0
            if secondCard == 10:
                secondCard = 0
        if firstCard > secondCard:
            firstHandWins = True
            break
        elif firstCard < secondCard:
            firstHandWins = False
            break
    return firstHandWins

# Check whatever hand (list) you feed into it
def handChecker(hand):
    cardRange = range(1, 14)
    currentType = 0
    jokerCount = 0
    cardCounter = [0, 0]
    # Check if hand has any Jokers (J = 10):
    if isPart2 and 10 in hand:
        jokerCount = hand.count(10)
    for card in cardRange:
        if isPart2 and hand.count(card) > 0 and not card == 10:
            cardAmount = hand.count(card) + jokerCount
        else:
            cardAmount = hand.count(card)
        if cardAmount > 0:
            cardCounter.append(cardAmount)
    cardCounter.sort(reverse=True)
    firstHighest = cardCounter[0]
    secondHighest = cardCounter[1]
    # Make sure Joker is only used for the highest count
    if jokerCount > 0:
        secondHighest = secondHighest - jokerCount
    # Check High Card
    if firstHighest == 0:
        currentType = 1
    # Check One Pair
    elif firstHighest == 2 and secondHighest < 2:
        currentType = 2
    # Check Two Pair
    elif firstHighest == 2 and secondHighest == 2:
        currentType = 3
    # Check Three of a Kind
    elif firstHighest == 3 and secondHighest < 2:
        currentType = 4
    # Check Full house
    elif firstHighest == 3 and secondHighest == 2:
        currentType = 5
    # Check Four of a Kind
    elif firstHighest == 4:
        currentType = 6
    # Check Five of a Kind
    elif firstHighest == 5:
        currentType = 7
    return currentType

def scoreinator(rankedList):
    rank = 0
    scoreList = []
    for handbid in rankedList:
        rank = rank + 1
        bid = handbid[1]
        score = bid * rank
        scoreList.append(score)
    output = sum(scoreList)
    return output

def initial(gameList):
    # Gotta rank them games
    rankedList = []
    for game in gameList:
        if not rankedList:
            rankedList.append(game)
        else:
            rankedList = rankinator(game, rankedList)
    # Gotta math the scores
    answer = scoreinator(rankedList)
    return answer

if __name__ == '__main__':
    isPart2 = False
    part1 = initial(gameList)
    part1Runtime = time.time() - startTime
    print(f"Part 1 answer: {part1}, finished in {part1Runtime}")

    isPart2 = True
    part2 = initial(gameList)
    part2Runtime = time.time() - startTime
    print(f"Part 2 answer: {part2}, finished in {part2Runtime}")