"""
Advent of Code Day 6 part 2
Hector Ramos
1/10/2016
"""
from input6 import s

def lightGrid(s):
    lines = s.split("\n")
    matrix = [[0 for x in xrange(1000)] for x in xrange(1000)]

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

    totalBrightness = 0

    for i in xrange(1000):
        for j in xrange(1000):
            if matrix[i][j]:
                totalBrightness += matrix[i][j]

    return "The total brightness of all lights is %d." %totalBrightness


def toggleLights(start, end, matrix):
    xStart = int(start[0])
    xEnd = int(end[0]) + 1
    yStart = int(start[1])
    yEnd = int(end[1]) + 1

    for i in xrange(xStart, xEnd):
        for j in xrange(yStart, yEnd):
            matrix[i][j] += 2

def turnOnLights(start, end, matrix):
    xStart = int(start[0])
    xEnd = int(end[0]) + 1
    yStart = int(start[1])
    yEnd = int(end[1]) + 1

    for i in xrange(xStart, xEnd):
        for j in xrange(yStart, yEnd):
            matrix[i][j] += 1

def turnOffLights(start, end, matrix):
    xStart = int(start[0])
    xEnd = int(end[0]) + 1
    yStart = int(start[1])
    yEnd = int(end[1]) + 1

    for i in xrange(xStart, xEnd):
        for j in xrange(yStart, yEnd):
            matrix[i][j] -= 1

            if matrix[i][j] < 0:
                matrix[i][j] = 0


print lightGrid(s)