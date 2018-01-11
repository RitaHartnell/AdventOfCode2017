# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 00:18:42 2017

@author: melso
"""

def groupValue(iStr):
    val = 0
    multiplier = 1
    for c in iStr:
        if c == "{":
            val += 1*multiplier
            multiplier += 1
        if c == "}":
            multiplier -= 1
    return val
 
def markNSweep(iStr):
    inGarbage = False
    isCanceled = False
    iStrNew = ""
    
    for i in range (len(iStr)):
        if inGarbage == True: #check for cancels and garbage end in garbage
            if iStr[i] == ">" and isCanceled == False: #end of garbage
                inGarbage = False
            elif iStr[i] == "!" and isCanceled == False:
                isCanceled = True
            elif isCanceled == True:
                isCanceled = False
        elif iStr[i] == "<" and inGarbage == False: #garbage start
            inGarbage = True
        elif inGarbage == False:
            iStrNew = iStrNew + iStr[i]
    
    return iStrNew

def markNCount(iStr):
    inGarbage = False
    isCanceled = False
    garbageNum = 0
    
    for i in range (len(iStr)):
        if inGarbage == True: #check for cancels and garbage end in garbage
            if iStr[i] == ">" and isCanceled == False: #end of garbage
                inGarbage = False
            elif iStr[i] == "!" and isCanceled == False:
                isCanceled = True
            elif isCanceled == True:
                isCanceled = False
            elif isCanceled == False: #if it's not a special character and not canceled, count it
                garbageNum += 1
        elif iStr[i] == "<" and inGarbage == False: #garbage start
            inGarbage = True
    
    return garbageNum

def fileOpen(iStr):
    with open(iStr, 'r') as rfile:
        inputstring = rfile.read()
    return inputstring

def main():
    filename = "AoC9.txt"
    inputfile = fileOpen(filename)
    """
    testString1 = "{<{},{},{{}}>}"
    testString2 = "{{<!>},{<!>},{<!>},{<a>}}"
    testString3 = "{{{},{},{{}}}}"
    
    finalStr = markNSweep(testString1)
    print(finalStr)
    value = groupValue(finalStr)
    print(value)
    finalStr = markNSweep(testString2)
    print(finalStr)
    value = groupValue(finalStr)
    print(value)
    finalStr = markNSweep(testString3)
    print(finalStr)
    value = groupValue(finalStr)
    print(value)
    """
    finalStr = markNSweep(inputfile)
    #print(finalStr)
    value = groupValue(finalStr)
    print(value)
    """
    print(markNCount(testString1))
    print(markNCount(testString2))
    print(markNCount(testString3))
    """
    print(markNCount(inputfile))

# =============================================================================
if __name__ == "__main__":
    main()
    
    