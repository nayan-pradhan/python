# Nayan Man Singh Pradhan

# Stack Class
class Stack:

    # initialize stack
    def __init__(self, stack_size):
        self.array = [None] * stack_size
        self.stack_size = stack_size
        self.top = 0

    # bool to check if stack is empty or not
    def isEmpty (self):
        print("Stack is empty? -> ", end = '')
        return self.top == 0
    
    # add elements to stack
    def push(self, elem):
        if self.top  == self.stack_size:
            return "stack overflow! unable to push {}!".format(elem)
        self.array[self.top] = elem
        self.top = self.top + 1
        return ("{} pushed to stack!".format(elem))
    
    # remove elements from stack
    def pop(self):
        if self.top == 0:
            return "stack underflow! nothing to pop!"
        temp = self.array[self.top - 1]
        del self.array[self.top - 1]
        self.top = self.top - 1
        return ("popping {}".format(temp)) # printing what is popped

    def topElem(self):
        if self.top != 0:
            print ("top elem is", end = ' ')
            return self.array[self.top-1]
        else:
            return "stack underflow! no top element!"

    # print stack
    def print(self):
        if self.top == 0:
            print ("nothing to print!")
        else:
            for elem in self.array:
                if elem != None:
                    print("{}".format(elem), end = ' ')
            print()

# stack1
myStack1 = Stack(2)
print(myStack1.isEmpty())
print(myStack1.push(1))
print(myStack1.isEmpty())
print(myStack1.push(2))
print(myStack1.push(3))
print(myStack1.isEmpty())
myStack1.print()
print(myStack1.topElem())
print(myStack1.pop())
myStack1.print()
print(myStack1.pop())
print(myStack1.pop())
myStack1.print()
print(myStack1.isEmpty())

# stack2
myStack2 = Stack(5)
print(myStack2.isEmpty())
print(myStack2.push(1))
print(myStack2.isEmpty())
print(myStack2.push(2))
myStack2.print()
print(myStack2.push(3))
print(myStack2.push(4))
print(myStack2.isEmpty())
myStack2.print()
print(myStack2.topElem())
print(myStack2.pop())
myStack2.print()
print(myStack2.pop())
print(myStack2.pop())
myStack2.print()
print(myStack2.isEmpty())