# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 20:11:26 2017

@author: melso
"""
context = { 'bottom': True, 'right': False, 'top': False, 'left': False, 'x': 0, 'y': 0, 'side_length': 1, 'current_thing': 0}

class Point:
    def __init__(self, value=0, xcoord=0, ycoord=0):
        self.val = value
        self.x = xcoord
        self.y = ycoord
    
    def isNextTo(self, Point):
        if abs(self.x - Point.x) <= 1 and abs(self.y - Point.y) <= 1:
            return True
        else:
            return False

def spiraler():
    global context
    if context['bottom']:
        context['x'] += 1
        context['current_thing'] += 1
        if context['current_thing'] == context['side_length']:
            context['current_thing'] = 0
            context['side_length'] += 2
            context['bottom'] = False
            context['right'] = True
            return
    elif context['right']:
        context['y'] +=1
        context['current_thing'] +=1
        if context['current_thing'] == context['side_length'] - 2:
            context['current_thing'] = 0
            context['right'] = False
            context['top'] = True
            return
    elif context['top']:
        context['x'] -=1
        context['current_thing'] += 1
        if context['current_thing'] == context['side_length'] - 1:
            context['current_thing'] = 0
            context['top'] = False
            context['left'] = True
            return
    elif context['left']:
        context['y'] -= 1
        context['current_thing'] += 1
        if context['current_thing'] == context['side_length'] - 1:
            context['current_thing'] = 0
            context['left'] = False
            context['bottom'] = True
    
def main():
    input = 277678
    points = []
    points.append(Point(value=1,xcoord=0,ycoord=0))
    biggie = 0
    for i in range (2, input+1):
        spiraler()
        newPoint = Point(value=0, xcoord=context['x'], ycoord=context['y'])
        
        """
        for j in range (0, len(points)):
            if points[j].isNextTo(points[i-1]):
                points[i-1].val += points[j].val 
        #"""
    
        for point in points:
            if point.isNextTo(newPoint):
                newPoint.val += point.val
        points.append(newPoint)
    
        """
        if points[i-1].val > input:
            biggie = points[i-1].val
            break
        """
        
        # Are we done?
        if newPoint.val > input:
            biggie = newPoint.val
            break
    
    for element in points:
        print("Value: %s" % element.val)
    coords = (context['x'], context['y'])
    print(coords)
    distance = abs(coords[0]) + abs(coords[1])
    print(distance)
    print(biggie)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    main()