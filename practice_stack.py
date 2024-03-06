
class Node:
    #"""Represents a node in the linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    #"""Implements a stack data structure."""
    def __init__(self, value=None):
        #"""Initializes the stack with an optional initial value."""
        if value is not None:
            self.top = Node(value)
            self.height = 1
        else:
            self.top = None
            self.height = 0

    def push(self, value):
        #"""Adds an item to the top of the stack."""
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def print_stack(self):
        #"""Prints all elements in the stack."""
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def pop(self):
        #Removes and returns the top element of the stack."""
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.height -= 1
            return temp.value

    def peak(self):
        #Returns the top element of the stack without removing it."""
        if self.top is None:
            return None
        else:
            return self.top.value
        
_stack = Stack(None)
_stack.push(10)
_stack.push(30)
print('\nprinting the stack after push(10) and push(30)\n')
_stack.print_stack()
_stack.pop()
print('printing the stack after the pop() method')
_stack.print_stack()
# calling push(80)
_stack.push(80)
print('\nPrinting the stack after push(80)')
_stack.print_stack()
# calling pop() 
_stack.pop()
print('\nPrinting stack after calling pop()\n')
_stack.print_stack()


