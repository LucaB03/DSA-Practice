class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
        else:
            new.next = self.head
            self.head = new


llist = LinkedList()
llist.insert("Hello")
llist.insert("World")
llist.insert("!")
node = llist.head
while node:
    print(node.data)
    node = node.next
