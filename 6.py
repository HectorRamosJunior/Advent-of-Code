"""
Advent of Code Day 6
Hector Ramos
1/10/2016
"""
from input6 import s

def lightGrid(s):
    lines = s.split("\n")
    matrix = [[False for x in xrange(1000)] for x in xrange(1000)]

    for l in lines:
        command = l.split(" ")

        if len(command) == 4:
            start = command[1].split(",")
            end = command[3].split(",")

            toggleLights(start, end, matrix)
        elif command[1] == "on":
            start = command[2].split(",")
            end = command[4].split(",")

            turnOnLights(start, end, matrix)
        elif command[1] == "off":
            start = command[2].split(",")
            end = command[4].split(",")

            turnOffLights(start, end, matrix)

    lightsOn = 0

    for i in xrange(1000):
        for j in xrange(1000):
            if matrix[i][j]:
                lightsOn += 1

    return "There are %d lights lit." %lightsOn


def toggleLights(start, end, matrix):
    xStart = int(start[0])
    xEnd = int(end[0]) + 1
    yStart = int(start[1])
    yEnd = int(end[1]) + 1

    for i in xrange(xStart, xEnd):
        for j in xrange(yStart, yEnd):
            matrix[i][j] = not matrix[i][j]

def turnOnLights(start, end, matrix):
    xStart = int(start[0])
    xEnd = int(end[0]) + 1
    yStart = int(start[1])
    yEnd = int(end[1]) + 1

    for i in xrange(xStart, xEnd):
        for j in xrange(yStart, yEnd):
            matrix[i][j] = True

def turnOffLights(start, end, matrix):
    xStart = int(start[0])
    xEnd = int(end[0]) + 1
    yStart = int(start[1])
    yEnd = int(end[1]) + 1

    for i in xrange(xStart, xEnd):
        for j in xrange(yStart, yEnd):
            matrix[i][j] = False


print lightGrid(s)