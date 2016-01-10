"""
Advent of Code Day 5
Hector Ramos
1/10/2016
"""
from input5 import s

def getNiceStrings(s):
    strings = s.split("\n")

    niceStringCount = 0
    for s in strings:
        vowelCount = 0
        previous = None
        doubleCharacter = False
        naughtyString = False

        for c in s:
            if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
                vowelCount += 1

            if not previous:
                previous = c
            elif previous == c:
                doubleCharacter = True
            elif previous == "a" and c == "b":
                naughtyString = True
            elif previous == "c" and c == "d":
                naughtyString = True
            elif previous == "p" and c == "q":
                naughtyString = True
            elif previous == "x" and c == "y":
                naughtyString = True

            previous = c 

        if vowelCount >= 3 and doubleCharacter and not naughtyString:
            niceStringCount += 1

    return "There are %d nice strings." %niceStringCount

def getNiceStrings2(s):
    strings = s.split("\n")

    niceStringCount = 0
    for s in strings:
        previous1 = None
        previous2 = None  

        pairDict = {} 
        repeatingCharacter = False
        repeatingPair = False

        for i in xrange(len(s)):
            #Repeating Pair Check, key is the concat of the pair
            if previous1 and (previous1 + s[i]) in pairDict:
                endIndex = pairDict[previous1 + s[i]]

                #Can't overlap from the dictionary entry
                if endIndex != i-1:
                    repeatingPair = True

            #Repeating Character Check
            if previous2 and previous2 == s[i]:
                repeatingCharacter = True

            if not previous1:
                previous1 = s[i]
            else:
                pairDict[previous1 + s[i]] = i
                previous2 = previous1 
                previous1 = s[i]

        if repeatingCharacter and repeatingPair:
            niceStringCount += 1

    return "There are %d nice strings." %niceStringCount


print getNiceStrings(s)
print getNiceStrings2(s)


