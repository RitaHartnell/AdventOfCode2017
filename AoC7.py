# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 18:29:48 2017

@author: melso
"""

class Node():
    def __init__(self, name, weight = 0, parent = None):
        self.name = name
        self.weight = weight
        self.parent = parent 
        self.children = []
        
    def setParent(self, parent):
        self.parent = parent
    
    def setWeight(self, weight):
        self.weight = weight
        
    def addChild(self, childNodeName, childNodeWeight):
        childNode = Node(name = childNodeName, weight = childNodeWeight, parent = self)
        self.children.append(childNode)
    
    def hasParent(self):
        if self.parent != None:
            return True
        return False
    
    def hasChildren(self):
        if not self.children:
            return False
        return True
    
    def copyNode(self):
        nodeCopy = Node(self.name, self.weight, self.parent)
        return nodeCopy
    
    def discWeight(self):    
        sum = self.weight
        if self.hasChildren() == False:
            return sum
        else:
            for child in self.children:
                sum += child.discWeight()
        return sum
    
def oddOneOut(iList):
    valueCount = {}
    for value in iList:
        if value in valueCount:
            valueCount[value] += 1
        else:
            valueCount[value] = 1
            
    odd_value = None
    for value in valueCount:
        if valueCount[value] == 1:
            odd_value = value
            
    for i in range(len(iList)):
        if iList[i] == odd_value:
            return i
    return None

def findProblem(inode):
    weights = []
    for child in inode.children:
        weights.append(child.discWeight())
    #print(weights)   
    
    index = oddOneOut(weights)
    print(index)    
    
    if index != None:
        new = findProblem(inode.children[index])
        #print(inode.children[index].weight)
        if new == False:
            diff = weights[index] - weights[(index+1)%len(weights)]
            print( inode.children[index].weight - diff)
        
    else: 
        print("It's my parents problem~")
        return False
    
def main():

    with open("AoC7.csv", 'r') as rfile:
        inputMess = rfile.read()
    
    inputMess = inputMess.split('\n')
    #print(inputMess[1])
    
    """ 
    for line in inputMess:
        line = line.split(" ")
        print(line)
        #line = list(split)
    """
    for i in range (len(inputMess)):
        inputMess[i] = inputMess[i].split(" ")
    
    #print(inputMess[1])
    
    replacement_table = dict.fromkeys(map(ord, "(),->"), None)
    
    #print(inputMess[1][0])
    
    
    for i in range (len(inputMess)):
        for j in range(len(inputMess[i])):
           inputMess[i][j] = inputMess[i][j].translate(replacement_table)
    
    """
    for line in inputMess:
        for string in line:
            string = string.translate(replacement_table)
    
    """   
    finalInput = []
    inputInside = []
    
    for line in inputMess:
        for string in line:
            if string != '':
                inputInside.append(string)
        finalInput.append(inputInside)
        inputInside = []
        
    #print(finalInput[1])
    
    nodes = []
    nodeList = []
    count = 0
    
    for line in finalInput:
        nodeList.append(Node(line[0], int(line[1])))
        
        #print(nodeList[count].name)
                     
        if len(line) != 2: #this is a leaf node with children
            for i in range (2, len(line)):
                nodeList[count].addChild(line[i], childNodeWeight = 0)
            #add all the children at the end
           # print(nodeList[count].name)
            #print(" ")
            for child in nodeList[count].children:
                nodes.append(child)
                #print(child.name)
            #print(" ")
            #check if their child is in nodeList already... add themseves as the parent if that's the case
            for i in range (len(nodeList)-1):
                for j in range (len(nodeList[count].children)):
                    if nodeList[count].children[j].name == nodeList[i].name:
                        nodeList[i].setParent(nodeList[count])
                        nodeList[count].children[j].setWeight(nodeList[i].weight)
                        nodeList[count].children[j].children = list(nodeList[i].children)
            """
            for child in nodeList[count].children:
                print(child.name)
            print(" ")"""
            
        #was the node added by it's parent?
        for i in range(len(nodes)):
            if nodes[i].name == nodeList[count].name:
                 nodeList[count].setParent(nodes[i].parent)
                 nodes[i].setWeight(nodeList[count].weight)
                 nodes[i].children = list(nodeList[count].children)
        count +=1
    #now that we have a list of all the nodes... find the one without a parent
    """
    for node in nodeList:
        print(node.name)
   
    for child in nodeList[10].children:
        print(child.name)
    print(" ")  """
    for node in nodeList:
        if node.hasParent() == False:
            print("Found it!")
            print("The root is: ", node.name)
            root = node
    
    #find the problem node
    findProblem(root)
    
    #newWeight = root.children[index].weight - diff
    #print("The new weight needs to be: %d" %newWeight)
    
if __name__ == '__main__':
    main()