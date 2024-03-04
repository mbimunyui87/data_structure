# creating the node class that will be called in the stack class to create the node
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

# Building the stack class 
class my_stack():
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
    def pop(self):
        if self.height == 0:
            return None
        elif self.height == 1:
            temp = self.top
            self.top = None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
        self.height -= 1
        return temp

_stack = my_stack(4)
_stack.push('test')
_stack.push(['stop', 'start', 'running'])
_stack.print_stack()
print(_stack.pop())
_stack.print_stack()
print(_stack.height)