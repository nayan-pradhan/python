# Nayan Man Singh Pradhan
# Still working on this file

# Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# LinkedList
class LinkedList:
    def __init__(self, numberOfElem): 
        self.numOfElem = numberOfElem
        self.head = None
        self.tail = None
    
    def addToFront(self, newElem):
        if self.numOfElem == 0:
            LinkedList.head = newElem
            LinkedList.tail = newElem
            newElem.next = None
            newElem.prev = None
        else:
            newElem.next = LinkedList
            LinkedList.head.next = newElem
            newElem.prev = None
            LinkedList.head = newElem
        self.numOfElem = self.numOfElem + 1
        return True
        