"""
Advent of Code Day 7
Hector Ramos
1/10/2016
"""
from input7 import s

def logicGates(s):
    lines = s.split("\n")

    wireDict = {}
    for l in lines:
        command = l.split(" ")

        if len(command) == 3: #Set
            wireDict[command[2]] = int(command[0])
        elif len(command) == 4: #NOT
            wireDict[command[3] = ~wireDict[command[1]] & 0xffff
        elif command[1] == "AND":
            wireDict[command[4]] = wireDict[command[0]] & wireDict[command[2]]
        elif command[1] == "OR":
            wireDict[command[4]] = wireDict[command[0]] | wireDict[command[2]]
        elif command[1] == "LSHIFT":
            wireDict[command[4]] = wireDict[command[0]] << command[2]
        elif command[1] == "RSHIFT":
            wireDict[command[4]] = wireDict[command[0]] >> command[2]

    return "The signal provided to wire a is %d" %wireDict["a"]

print logicGates(s)
