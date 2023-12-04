with open("input.txt", "r") as inputfile:
    cardList = []
    for line in inputfile:
        winningnumbers, playingnumbers = line.split("|")
        cardnumber, winningnumbers = winningnumbers.split(":")
        cardnumber = cardnumber.replace("Card ", "").strip()
        winningnumbers = winningnumbers.split()
        playingnumbers = playingnumbers.split()
        cardList.append([int(cardnumber), winningnumbers, playingnumbers])

def cardchecker(cardList, isPart2):
    answer, points, matches = 0, 0, 0
    for card in cardList:
        cardnumber = card[0]
        winningnumbers = card[1]
        playingnumbers = card[2]
        print(f"Checking card {cardnumber} (index {cardnumber-1}):")
        print(f"Winning numbers: {card[1]}")
        print(f"Playing numbers: {card[2]}")
        for number in winningnumbers:
            matches = matches + playingnumbers.count(number)
        print(f"Number of matches is {matches}")
        if isPart2:
            if matches > 0:
                for copies in range(cardnumber, cardnumber+matches, 1):
                    print(f"Making copy of card {copies+1}, index {copies}.")
                    print(cardList[copies])
                    cardList.append(cardList[copies])
                answer = len(cardList)
        else:
            if matches > 1:
                points = 1 * 2 ** (matches-1)
                print(points)
            else:
                points = matches
                print(points)
            answer = answer + points
        matches = 0
    return answer

answer = cardchecker(cardList, False)
print(f"Part 1 is: {answer}")
answer = cardchecker(cardList, True)
print(f"Part 2 is: {answer}")