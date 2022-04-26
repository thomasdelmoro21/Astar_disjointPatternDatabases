'''
@author Thomas Del Moro
'''


class Element:
    def __init__(self, v):
        self.value = v
        self.dx = 0
        self.dy = 0

def linearConflicts(node, length):
    d = 0
    elements = []
    conflicts = 0
    for i in range(len(node)):
        element = Element(node[i])
        if element.value != 0:
            element.dx = abs((element.value % length) - (i % length))
            d += element.dx
            element.dy = abs((element.value // length) - (i // length))
            d += element.dy
        elements.append(element)

    #rowConflicts
    for i in range(0, length):
        for j in range(0, length-1):
            currentElement = elements[i*length+j]
            if currentElement.dy == 0 and currentElement.value != 0:
                for k in range(j+1, length):
                    conflictElement = elements[i*length+k]
                    if conflictElement.dy == 0 and currentElement.value > conflictElement.value != 0:
                        conflicts += 1
                        break

    #columnConflicts
    for j in range(0, length):
        for i in range(0, length-1):
            currentElement = elements[i*length+j]
            if currentElement.dx == 0 and currentElement.value != 0:
                for k in range(i+1, length):
                    conflictElement = elements[k*length+j]
                    if conflictElement.dx == 0 and currentElement.value > conflictElement.value != 0:
                        conflicts += 1
                        break

    d += conflicts * 2
    return d
