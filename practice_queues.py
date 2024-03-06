class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class MyQueue:
    def __init__(self, value=None):
        self.first = None
        self.last = None
        self.size = 0
        if value is not None:
            self.enqueue(value)

    def enqueue(self, value):
        new_node = Node(value)
        if self.size == 0:
            self.first = new_node
        else:
            self.last.next = new_node
        self.last = new_node
        self.size += 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            temp = self.first
            self.first = self.first.next
            temp.next = None
            self.size -= 1
            return temp.value

    def peek(self):
        #Retrieves the element from the front of the queue without deleting it.
        if self.first is not None:
            return self.first.value
        else:
            return None

    def rear(self):
        #Returns an element from the rear end of the queue.
        if self.last is not None:
            return self.last.value
        else:
            return None

# Example usage:
queue = MyQueue(45)
queue.enqueue(8)
queue.enqueue(4)
queue.print_queue()
print("Peek value:", queue.peek())
print("Rear value:", queue.rear())
