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

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next

    def delete(self, data):
        prev = self.head
        current = prev.next
        if prev.data == data:
            self.head = self.head.next
            return True
        while current:
            if current.data == data:
                prev.next = current.next if current.next else None
                return True
            prev = current
            current = current.next
        return False

    def length(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    def reverse(self):
        reverse = LinkedList()
        current = self.head
        while current:
            reverse.insert(current.data)
            current = current.next
        self.head = reverse.head


# Traversing and printing
llist = LinkedList()
llist.insert("Hello")
llist.insert("World")
llist.insert("!")
node = llist.head
while node:
    print(node.data)
    node = node.next
