# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 19:31:40 2017

@author: melso
"""

import AoC9 as op

def distance(x,y):
    dx = abs(x)
    dy = abs(y)
    
    curX = dx
    curY = dy
    steps = 0
    
    while curX != 0 and curY != 0:
        curX -= 1
        curY -= 1
        steps += 1
        #print(curX,curY,steps)
    
    return steps + curX + curY
    
def hexer(iList):
    x = 0
    y = 0
    
    for direction in iList:
        if direction == "n":
            y += 1
        elif direction == "s":
            y -= 1
        elif direction == "ne":
            x += 1
        elif direction == "sw":
            x -= 1
        elif direction == "nw":
            y += 1
            x -= 1
        elif direction == "se":
            y -= 1
            x += 1
        
    print(x,y)
    if (x>0 and y<0) or (x<0 and y>0):
        iDistance = distance(x,y)
    else:
        iDistance = abs(x) + abs(y)
    return iDistance

def hexerOneAtATime(iList):
    x = 0
    y = 0
    biggestEver = 0
    currentDist = 0
    
    for direction in iList:
        if direction == "n":
            y += 1
        elif direction == "s":
            y -= 1
        elif direction == "ne":
            x += 1
        elif direction == "sw":
            x -= 1
        elif direction == "nw":
            y += 1
            x -= 1
        elif direction == "se":
            y -= 1
            x += 1
        if (x>0 and y<0) or (x<0 and y>0):
            currentDist = distance(x,y)
        else:
            currentDist = abs(x) + abs(y)
        
        if currentDist > biggestEver:
            biggestEver = currentDist
    
    return biggestEver
    
    
def main():
    inputFile = "AoC11.txt"
    inputStr = op.fileOpen(inputFile)
    inputList = inputStr.split(",")
    value = hexer(inputList)
    print(value)
    """
    list1 = ["ne", "ne", "ne"]
    val1 = hexer(list1)
    print(val1)
    list2 = ["ne", "ne", "sw", "sw"]
    val2 = hexer(list2)
    print(val2)
    list3 = ["ne", "ne", "s", "s"]
    val3 = hexer(list3)
    print(val3)
    str4 = "se,sw,se,sw,sw"
    list4 = str4.split(",")
    val4 = hexer(list4)
    print(val4)
    #"""
    biggest = hexerOneAtATime(inputList)
    print(biggest)
    
    
if __name__ == "__main__":
    main()