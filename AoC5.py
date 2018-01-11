# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 18:25:32 2017

@author: melso
"""

def jump(list):
    i = 0
    count = 0
    while i < len(list):
        placeholder = i
        i += list[i]
        list[placeholder] += 1
        count += 1
    return count

def jump2(list):
    i = 0
    count = 0
    while i < len(list):
        placeholder = i
        i += list[i]
        if list[placeholder] >= 3:
            list[placeholder] -= 1
        else:
            list[placeholder] += 1   
        count += 1
    return count

def main():
    inputs = []
    with open("AoC5.csv", 'r') as rfile:
        data = rfile.read()
        
    data = data.split('\n')
    
    for item in data:
        inputs.append(int(item))
    
    jumps = jump(inputs)
    jumps2 = jump2(inputs)
    
    print("The number of jumps for part one is: %d" % jumps)
    print("The number of jumps for part two is: %d" % jumps2)
    
if __name__ == '__main__':
    main()