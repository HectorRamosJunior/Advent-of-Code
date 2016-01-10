"""
Advent of Code Day 4
Hector Ramos
1/9/2016
"""
import hashlib

def firstFiveZeroHash(key):
    counter = 0

    while True:
        h = hashlib.md5()
        h.update(key + str(counter))
        hashResult = h.hexdigest()

        if hashResult.startswith("000000") == True:
            return "The lowest number is %d" %counter

        counter += 1

print firstFiveZeroHash("iwrupvqb")