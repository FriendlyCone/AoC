import re

with open("input.txt", "r") as inputfile:
    # Input looks like:
    # Game 1: 4 red, 1 green, 15 blue; 6 green, 2 red, 10 blue; 7 blue, 6 green, 4 red; 12 blue, 10 green, 3 red
        gamelist = []
        for line in inputfile:
            line = line.replace("Game ", "")
            gamelist.append(line.split(": "))

def gameprocessor(game):
    gameID = int(game[0])
    gameRED = re.findall(r"([0-9]*) red", game[1])
    gameRED = [int(item) for item in gameRED]
    gameREDmax = max(gameRED)
    gameGREEN = re.findall(r"([0-9]*) green", game[1])
    gameGREEN = [int(item) for item in gameGREEN]
    gameGREENmax = max(gameGREEN)
    gameBLUE = re.findall(r"([0-9]*) blue", game[1])
    gameBLUE = [int(item) for item in gameBLUE]
    gameBLUEmax = max(gameBLUE)
    return gameID, gameRED, gameGREEN, gameBLUE, gameREDmax, gameGREENmax, gameBLUEmax

def gamevalidator(gameRED, gameGREEN, gameBLUE):
    valid = True
    for red in gameRED:
        if red > 12:
            valid = False
            return valid
    for green in gameGREEN:
        if green > 13:
            valid = False
            return valid
    for blue in gameBLUE:
        if blue > 14:
            valid = False
            return valid
    return valid

sumID = 0
sumsetpower = 0
for game in gamelist:
    gameID, gameRED, gameGREEN, gameBLUE, gameREDmax, gameGREENmax, gameBLUEmax = gameprocessor(game)
    valid = gamevalidator(gameRED, gameGREEN, gameBLUE)
    if valid:
        sumID = sumID + gameID
    setpower = gameREDmax * gameGREENmax * gameBLUEmax
    sumsetpower = sumsetpower + setpower
        
print(sumID)
print(sumsetpower)