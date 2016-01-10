"""
Advent of Code Day 2
Hector Ramos
1/10/2016
"""
from input2 import s    #string input was rather long

def wrappingPaperAmount(s):
    lines = s.split("\n")
    dimensions = []
    for l in lines:
        dimensions.append(l.split("x"))

    wrappingPaper = 0
    ribbon = 0
    for box in dimensions:
        l, w, h = box

        l = int(l)
        w = int(w)
        h = int(h)

        side1 = l*w 
        side2 = w*h 
        side3 = l*h 

        wrappingPaper += 2*side1 + 2*side2 + 2*side3
        ribbon += l*w*h 

        if l <= h and w <= h:
            wrappingPaper += side1
            ribbon += 2*l + 2*w
        elif w <= l and h <= l:
            wrappingPaper += side2
            ribbon += 2*w + 2*h
        elif h <= w and l <= w:
            wrappingPaper += side3
            ribbon += 2*h + 2*l

    out = "%d sq ft of wrapping paper" %wrappingPaper
    out += ", %d of ribbon required!" %ribbon

    return out

print wrappingPaperAmount(s)