# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 00:18:30 2017

@author: melso
"""

def conditionChecker(iDict, iList):
    """
    This fuction returns true or false dependent on the truth of the operation condition 
    dictated by the second element and compares the key value of the register with the 3rd element
    of the list
    """
    reg = iList[0]
    op = iList[1]
    num = iList[2]
    if op == '==':
        return iDict[reg] == num
    elif op == '!=':
        return iDict[reg] != num
    elif op == '>=':
        return iDict[reg] >= num
    elif op == '<=':
        return iDict[reg] <= num
    elif op == '>':
        return iDict[reg] > num
    elif op == '<':
        return iDict[reg] < num

def operationChecker(iDict, iList):
    reg = iDict[iList[0]]
    op = iList[1]
    num = iList[2]
    
    if op == 'inc':
        return reg + num
    if op == 'dec':
        return reg - num
    

def main():
    #open out input file into a string called inputFile
    with open("AoC8.txt", 'r') as rfile:
        inputFile = rfile.read()
    
    
    #turn inputFile into a list of strings split  by a new line character
    inputFile = inputFile.split('\n')
    
    #declare two new lists... one for the +/- operation, the other for the if condition
    operation = []
    condition = []
    
    #we know what out input looks like... each line is of the format <x> inc/dec <num> if <y> <opperator> <num2>
    #so let's split each line up knowing this... removing the whitespaces from the start and end while we're at it
    for i in range(len(inputFile)):
        operation.append(inputFile[i].split('if')[0])
        operation[i] = operation[i].strip()
        condition.append(inputFile[i].split("if")[-1])
        condition[i] = condition[i].strip()
    
    print(operation[1])
    print(condition[1])
     
    #now lets go through the operation list and split it based on the spaces!
    for i in range(len(operation)):
        operation[i] = operation[i].split(" ")
        #now that that's out of the way, let's go ahead and make that last one an int, shall we?
        operation[i][2] = int(operation[i][2])
        
    print(operation[1])
    print(condition[1])
    
    #actually, we can do the exact same thing for condition as well, no?
    for i in range(len(condition)):
        condition[i] = condition[i].split(" ")
        condition[i][2] = int(condition[i][2])
    
    #now that we have out input all cleaned up, let's do something with it!
    #he default value for all of our registers is 0... so let's put them all as keys in a dict with a val of 0!
    
    registers = {}
    
    for register in operation:
        registers[register[0]] = 0
    
    #this part is modified to account for part two of the problem
    largestEver = 0    
    for i in range(len(operation)):
        if conditionChecker(registers, condition[i]) == True:
            registers[operation[i][0]] = operationChecker(registers, operation[i])
            if registers[operation[i][0]] > largestEver:
                largestEver = registers[operation[i][0]]
    
    #now we have (hopefully) completed the intructions in out input
    #we need to now go through and find the largest value!
    currentBiggest = 0
    
    for value in registers.values():
        if value > currentBiggest:
            currentBiggest = value
    
    print("The Largest key value is: %d" %currentBiggest)
    print("The largest key value ever was: %d" %largestEver)
    
#*****************************************************************************#    
if __name__ == '__main__':
    main()
    