class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1

    def get(self, index):
        if index >= self.length:
            return None
        current = self.head
        for i in range(index):
            current = current.next
        return current.data

    def remove(self, index):
        if index >= self.length:
            return
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.length -= 1

    def insert(self, n, val):
        if n >= self.length:
            self.push(val)
        elif n == 0:
            new_node = Node(val)
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        else:
            new_node = Node(val)
            current = self.head
            for i in range(n - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.length += 1

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next
            
test = LinkedList()
test.push(10)
test.push(20)
test.push(30)
for i in test:
    print(i)