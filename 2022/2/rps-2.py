inputfile = open("input.txt", "r")

# A = Rock = 1
# B = Paper = 2
# C = Scissors = 3
# X = Lose
# Y = Draw
# Z = Win

# Variables
score = 0

for line in inputfile:
    if "A" in line:
        # print("A")
        if "X" in line:
            # Rock vs Scissors = Loss
            score = score + 3 + 0
            print(f"Rock vs Scissors = Loss, current score: {score}")
        elif "Y" in line:
            # Rock vs Rock = Draw
            score = score + 1 + 3
            print(f"Rock vs Rock = Draw, current score: {score}")
        else:
            # Rock vs Paper = Win
            score = score + 2 + 6
            print(f"Rock vs Paper = Win, current score: {score}")
    elif "B" in line:
        # print("B")
        if "X" in line:
            # Paper vs Rock = Loss
            score = score + 1 + 0
            print(f"Paper vs Rock = Loss, current score: {score}")
        elif "Y" in line:
            # Paper vs Paper = Draw
            score = score + 2 + 3
            print(f"Paper vs Paper = Draw, current score: {score}")
        else:
            # Paper vs Scissors = Win
            score = score + 3 + 6
            print(f"Paper vs Scissors = Win, current score: {score}")
    else:
        # print("C")
        if "X" in line:
            # Scissors vs Paper = Loss
            score = score + 2 + 0
            print(f"Scissors vs Paper = Loss, current score: {score}")
        elif "Y" in line:
            # Scissors vs Scissors = Draw
            score = score + 3 + 3
            print(f"Scissors vs Scissors = Draw, current score: {score}")
        else:
            # Scissors vs Rock = Win
            score = score + 1 + 6
            print(f"Scissors vs Rock = Win, current score: {score}")
print(f"The final score is: {score}")