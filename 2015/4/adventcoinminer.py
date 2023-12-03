import hashlib

with open("input.txt", "r") as inputfile:
    input = inputfile.read()

def hashinator(input):
    number = 1
    zerohashfound_five = False
    zerohashfound_six = False
    while not zerohashfound_five or not zerohashfound_six:
        minechallenge = input + str(number)
        md5hash = hashlib.md5(minechallenge.encode())
        md5hashdecoded = md5hash.hexdigest()
        print(f"{minechallenge} results in {md5hashdecoded}") # This is for seeing all hashes and numbers, but massively slows down the process. Comment out to get the answer quick.
        if md5hashdecoded.startswith("00000") and not zerohashfound_five:
            zerohashfound_five = True
            minechallenge_five, md5hashdecoded_five, number_five = minechallenge, md5hashdecoded, str(number)
        if md5hashdecoded.startswith("000000") and not zerohashfound_six:
            zerohashfound_six = True
            minechallenge_six, md5hashdecoded_six, number_six = minechallenge, md5hashdecoded, str(number)
        number = number + 1
    return minechallenge_five, md5hashdecoded_five, number_five, minechallenge_six, md5hashdecoded_six, number_six

answerinput_five, answermd5_five, answernumber_five, answerinput_six, answermd5_six, answernumber_six = hashinator(input)
print(f"\n==== Found Answer! ====\nFive: {answerinput_five} results in {answermd5_five}\nThe answer number is {answernumber_five}\nSix: {answerinput_six} results in {answermd5_six}\nThe answer number is {answernumber_six}\n=======================")