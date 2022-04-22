'''
@author Thomas Del Moro
'''


class Element:
    def __init__(self, v):
        self.value = v
        self.dx = 0
        self.dy = 0

def linearConflicts(node):
    d = 0
    elements = []
    conflicts = 0
    for i in range(len(node)):
        element = Element(node[i])
        if element.value != 0:
            element.dx = abs((element.value % 4) - (i % 4))
            d += element.dx
            element.dy = abs((element.value // 4) - (i // 4))
            d += element.dy
        elements.append(element)

    #rowConflicts
    for i in range(0, 4):
        for j in range(0, 3):
            currentElement = elements[i*4+j]
            if currentElement.dy == 0 and currentElement.value != 0:
                for k in range(j+1, 4):
                    conflictElement = elements[i*4+k]
                    if currentElement.value > conflictElement.value != 0:
                        conflicts += 1

    #columnConflicts
    for j in range(0, 4):
        for i in range(0, 3):
            currentElement = elements[i*4+j]
            if currentElement.dx == 0 and currentElement.value != 0:
                for k in range(i+1, 4):
                    conflictElement = elements[k*4+j]
                    if currentElement.value > conflictElement.value != 0:
                        conflicts += 1

    d += conflicts * 2
    return d
