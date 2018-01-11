# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 19:34:52 2017

@author: melso
"""

original_input = "4	10	4	1	8	4	9	14	5	1	14	15	0	15	3	5"

# Redists the list and returns the new redisted list
def redistcycle(mem):
    redister = 0
    currentbig = 0
    for i in range (0, len(mem)):
        if mem[i] > redister:
            redister = mem[i]
            currentbig = i
    
    mem[currentbig] = 0
    
    while redister != 0:
        for i in range (0, len(mem)):
            j = ( currentbig + i + 1 ) % len(mem)
            mem[j] += 1
            redister -= 1
            if redister <= 0:
                break
    return mem
    
# Returns the list (mem) as a string that can be stored into a dict
def statemaker(mem):
    stringy = ""
    for blocks in mem:
        stringy = stringy + " " + str(blocks)
    return stringy

def main():
    input_list = original_input.split('\t')
    int_list = []
    
    # Turn all elements in the input list to ints
    for item in input_list:
        int_list.append(int(item))
    # By this point we have an int list that is guaranteed to be ints and formatted
    
    string_list = statemaker(int_list)
    
    # Let's make the dict to remember our states!
    states = { string_list: 0 }
    
    count = 0
    final_str = ""
    while True:
        int_list = redistcycle(int_list)
        redistedStr = statemaker(int_list)
        count += 1
        
        if redistedStr in states:
            # Oh shit, we found a loop
            final_str = redistedStr
            break
        else:
            # First time meeting this guy
            states[redistedStr] = count
        
    print(count - states[final_str])
    print(count)

if __name__ == "__main__":
    main()
        