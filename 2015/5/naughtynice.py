import string

naughtyniceList = []

with open("input.txt", "r") as inputfile:
    for line in inputfile:
        naughtyniceList.append(line.strip())

def part1nicenaughtycheck(naughtyniceList):
    nicestrings = 0
    vowelList = [ "a", "e", "i", "o", "u"]
    for littlekid in naughtyniceList:
        print(f"\n-- {littlekid} --")
        # check one: It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
        if "ab" in littlekid or "cd" in littlekid or "pq" in littlekid or "xy" in littlekid:
            print("Found naughty string!")
            continue
        else:
            print("Naughty string check passed...")
        # check two: It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
        littlekidList = [*littlekid]
        numvowels = 0
        for character in littlekidList:
            if character not in vowelList:
                continue
            else:
                numvowels = numvowels + 1
        if numvowels < 3:
            print("Not enough vowels!")
            continue
        else:
            print("Vowel check passed...")
        # check three: It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
        startCompare = 0
        endCompare = 2
        foundDouble = False
        for character in littlekidList:
            while endCompare < len(littlekidList) + 1 and not foundDouble:
                compareList = littlekidList[startCompare:endCompare]
                # print(compareList)
                startCompare = startCompare + 1
                endCompare = endCompare + 1
                doubleCheck = set(compareList)
                if len(doubleCheck) < len(compareList):
                    foundDouble = True
        if foundDouble:
            print("Found double letter! All checks passed.")
            # all checks passed, count as nice string
            nicestrings = nicestrings + 1
        else:
            print("No double letter found!")
    return nicestrings

def part2nicenaughtycheck(naughtyList):
    nicestrings = 0
    for littlekid in naughtyniceList:
        print(f"\n-- {littlekid} --")
        littlekidList = [*littlekid]
        # check one: It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
        startCompare = 0
        endCompare = 1
        foundDouble = False
        for character in littlekidList:
            while endCompare < len(littlekidList) and not foundDouble:
                #Make string of the 2 characters we use for comparison
                compareString = littlekidList[startCompare] + littlekidList[endCompare]
                #Make list of remainder, with a seperator character to prevent creating new matches
                compareList = littlekidList[0:startCompare] + ['_'] + littlekidList[endCompare+1:len(littlekidList)]
                #Make string of the sliced list to use for lazy comparison
                compareListString = ''.join([str(letter) for letter in compareList])
                startCompare = startCompare + 1
                endCompare = endCompare + 1
                if compareString in compareListString:
                    foundDouble = True
        if not foundDouble:
            print("No double set found!")
            continue
        else:
            print("Found double set...")

        # check two: It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
        startCompare = 0
        endCompare = 3
        foundDouble = False
        for character in littlekidList:
            while endCompare < len(littlekidList) + 1 and not foundDouble:
                compareList = littlekidList[startCompare:endCompare]
                startCompare = startCompare + 1
                endCompare = endCompare + 1
                compareList.pop(1)
                doubleCheck = set(compareList)
                if len(doubleCheck) < len(compareList):
                    foundDouble = True
        if foundDouble:
            print("Found spaced repeating letter! All checks passed.")
            # all checks passed, count as nice string
            nicestrings = nicestrings + 1
        else:
            print("No spaced repeating found!")
    return nicestrings

nicestrings1 = part1nicenaughtycheck(naughtyniceList)
nicestrings2 = part2nicenaughtycheck(naughtyniceList)
print(f"\nWe have {nicestrings1} nice strings according to Part 1 rules!")
print(f"We have {nicestrings2} nice strings according to Part 2 rules!")
print("Answer 399 is too high... 15 is wrong...")