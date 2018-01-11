# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 22:00:04 2017

@author: melso
"""

def genStandardList(size):
    retList = []
    for value in range(size):
        retList.append(value)
    return retList


def genIntListFromPuzzleInput(puzzle_input):
    retList = []
    puzzle_input = puzzle_input.split(',')
    for element in puzzle_input:
        retList.append(int(element))
    return retList


def getPartOneAnswer(stdList, lengthList):
    current_pos = 0
    skip_size = 0

    for length in lengthList:

        # Get the numbers to reverse in a list
        list_to_reverse = []
        for index in range(length):
            list_to_reverse.append(stdList[(current_pos + index) % len(stdList)])
        # Reverse the list
        list_to_reverse = list_to_reverse[::-1]

        # Inject list to reverse into std list
        for index in range(length):
            stdList[(current_pos + index) % len(stdList)] = list_to_reverse[index]

        # Update book keeping variables
        current_pos = (current_pos + length + skip_size) % len(stdList)
        skip_size += 1

    return stdList

def getASCIIListFromPuzzleInput(puzzle_input):
    manditoryEnding = [17, 31, 73, 47, 23]
    retList = []
    for char in puzzle_input:
        retList.append(ord(char))
    return retList + manditoryEnding


def genKnotHashRound(stdList, lengthList, current_pos, skip_size):
    for length in lengthList:

        # Get the numbers to reverse in a list
        list_to_reverse = []
        for index in range(length):
            list_to_reverse.append(stdList[(current_pos + index) % len(stdList)])
        # Reverse the list
        list_to_reverse = list_to_reverse[::-1]

        # Inject list to reverse into std list
        for index in range(length):
            stdList[(current_pos + index) % len(stdList)] = list_to_reverse[index]

        # Update book keeping variables
        current_pos = (current_pos + length + skip_size) % len(stdList)
        skip_size += 1

    return stdList, current_pos, skip_size


def genSparseHash(stdList, lengthList):
    current_pos = 0
    skip_size = 0
    for round in range(64):
        stdList, current_pos, skip_size = genKnotHashRound(stdList, lengthList, current_pos, skip_size)
    return stdList


def genDenseHash(sparseHash):
    denseHash = []

    masterIndex = 0
    for reduceRound in range(16):
        tmpList = []

        # Get 16 values from sparse hash for processing
        for sparseValue in range(16):
            tmpList.append(sparseHash[masterIndex])
            masterIndex += 1

        # Get the value to add into dense hash
        XORValue = tmpList[0]
        for tmpValue in tmpList[1:]:
            XORValue ^= tmpValue

        denseHash.append(XORValue)

    return denseHash


def genStdKnotHash(denseHash):

    knotHash = ""
    for num in denseHash:
        # Get the hex value
        hexValue = hex(num)[2:]

        if len(hexValue) == 1:
            hexValue = "0" + hexValue

        knotHash += hexValue
    print(knotHash)


def main():
    puzzle_input = "88,88,211,106,141,1,78,254,2,111,77,255,90,0,54,205"

    stdList = genStandardList(256)


    #stdList = [0, 1, 2, 3, 4]
    #lengthList = [3, 4, 1, 5]

    """
    # Part 1
    lengthList = genIntListFromPuzzleInput(puzzle_input)
    stdList = getPartOneAnswer(stdList, lengthList)
    print("Part 1: %s" % (stdList[0] * stdList[1]))
    #"""

    # Part 2
    #puzzle_input = "1,2,3"
    lengthList = getASCIIListFromPuzzleInput(puzzle_input)
    sparseList = genSparseHash(stdList, lengthList)
    denseList = genDenseHash(sparseList)
    knotHash = genStdKnotHash(denseList)

    #print(hex(5))


if __name__ == '__main__':
    main()
