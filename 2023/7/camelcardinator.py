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
# with open("D:/GitLabRepositories/adventofcode/advent-of-code/2023/7/input.txt", "r") as inputfile:
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
            # print(f"Comparing {currentcheckingHand} to {currentrankedHand}: {currentHandType}-{rankedHandType}. We win, place at {newPosition}")
            break
        # If we lose, do nothing unless its the last hand, then put it at the end.
        elif currentHandType < rankedHandType and not hadTieBreak:
            if rankedHand == rankList[-1]:
                # print(f"Comparing {currentcheckingHand} to {currentrankedHand}: {currentHandType}-{rankedHandType}. We lose, place at the end.")
                newrankList.append(checkingHand)
        # If the hand type is the same, put it in the tiebreaker.
        elif currentHandType == rankedHandType:
            currenthandWins = tieBreak(currentcheckingHand, currentrankedHand)
            # If we win the tiebreaker, put it in the loser's index.
            if currenthandWins:
                newPosition = newrankList.index(rankedHand)
                newrankList.insert(newPosition, checkingHand)
                hadTieBreak = False
                # print(f"Comparing {currentcheckingHand} to {currentrankedHand}: {currentHandType}-{rankedHandType}. We tie but win, place at {newPosition}")
                break
            else:
                newPosition = newrankList.index(rankedHand) + 1
                hadTieBreak = True
                # print(f"Comparing {currentcheckingHand} to {currentrankedHand}: {currentHandType}-{rankedHandType}. We tie and lose. Check next...")
                # print(f"DEBUG: {newPosition}")
        elif hadTieBreak:
            newrankList.insert(newPosition, checkingHand)
            hadTieBreak = False
            # print(f"Comparing {currentcheckingHand} to {currentrankedHand}: {currentHandType}-{rankedHandType}. We tied previously, run {newPosition}")
            break
    # print(f"Place at position: {newPosition}")
    if hadTieBreak:
        newrankList.insert(newPosition, checkingHand)
        hadTieBreak = False
        # print(f"Comparing {currentcheckingHand} to {currentrankedHand}: {currentHandType}-{rankedHandType}. We tied previously, run {newPosition}. This is the last hand to check.")
    # print(f"Current order: {newrankList}")
    newrankList.reverse()
    return newrankList

# Used for breaking ties
def tieBreak(firstHand, secondHand):
    for firstCard, secondCard in zip(firstHand, secondHand):
        if firstCard > secondCard:
            firstHandWins = True
            # print("Checking hand wins!")
            break
        elif firstCard < secondCard:
            firstHandWins = False
            # print("Checking hand loses!")
            break
    return firstHandWins

# Check whatever hand (list) you feed into it
def handChecker(hand):
    cardRange = range(1, 14)
    pairOne, pairTwo, HighCard = 0, 0, 0
    currentType = 0
    for card in cardRange:
        cardAmount = hand.count(card)
        # High Card (mainly saving the highest card)
        if cardAmount == 1:
            if currentType < 1:
                currentType = 1
            if not HighCard:
                HighCard = card
            elif card > HighCard:
                HighCard = card
        # One Pair
        if cardAmount == 2 and not pairOne:
            if currentType < 2:
                currentType = 2
            pairOne = card
        # Two Pair, break because 4 but no other hand possible
        elif cardAmount == 2 and pairOne:
            pairTwo = card
            currentType = 3
            break
        # Three of a kind
        if cardAmount == 3 and not pairOne:
            if currentType < 4:
                currentType = 4
            ThreeAK = card
        # Full House, break because 5
        elif cardAmount == 3 and pairOne:
            ThreeAK = card
            currentType = 5
            break
        # Four of a kind, break because 4 but no other hand possible
        if cardAmount == 4:
            FourAK = card
            currentType = 6
            break
        # Five of a kind, break because 5
        if cardAmount == 5:
            FiveAK = card
            currentType = 7
            break
    # print(f"Hand checker: {hand}, type {currentType}")
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
    print(rankedList)
    answer = scoreinator(rankedList)
    return answer

if __name__ == '__main__':
    part1 = initial(gameList)
    part1Runtime = time.time() - startTime
    print(f"Part 1 answer: {part1}, finished in {part1Runtime}")

    # part2 = initial(gameList)
    # part2Runtime = time.time() - startTime
    # print(f"Part 2 answer: {part2}, finished in {part2Runtime}")
    
    # 250178729 answer is too high
    # 250285767 answer is too high
    # 197443191 answer is wrong
    # 250178729