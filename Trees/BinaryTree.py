import math


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def delete(self, parent):
        # Node has 1 or 0 children
        if not self.left or not self.right:
            if self == parent.left:
                parent.left = self.left if self.left else self.right
            else:
                parent.right = self.left if self.left else self.right
        # Node has 2 children
        else:
            if self == parent.left:
                parent.left = self.left
            else:
                parent.right = self.left
            current = self.left
            while current.left:
                current = current.left
            current.left = self.right

    def calcHeight(self):
        lHeight = self.left.calcHeight() if self.left else 0
        rHeight = self.right.calcHeight() if self.right else 0
        return lHeight + 1 if lHeight > rHeight else rHeight + 1

    # Pre-Order, In-Order, Post-Order are all implementations of Depth-First-Traversal
    def travPreOrder(self):
        print(self.value)
        if self.left:
            self.left.travPreOrder()
        if self.right:
            self.right.travPreOrder()

    def travInOrder(self):
        if self.left:
            self.left.travInOrder()
        print(self.value)
        if self.right:
            self.right.travInOrder()

    def travPostOrder(self):
        if self.left:
            self.left.travPostOrder()
        if self.right:
            self.right.travPostOrder()
        print(self.value)

    # Implementation of Breadth-First-Traversal
    def travLevelOrder(self):
        queue = [self]
        while len(queue) > 0:
            print(queue[0].value)
            current = queue.pop(0)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    def toBST(self):
        order = []

        def InOrder(root):
            if root.left:
                InOrder(root.left)
            order.append(root.value)
            if root.right:
                InOrder(root.right)

        InOrder(self)
        it = iter(sorted(order))

        def transform(root):
            if root.left:
                transform(root.left)
            root.value = next(it)
            if root.right:
                transform(root.right)

        transform(self)

    # Only produces valid output if the input is a bst
    # Uses the Day-Stout-Warren algorithm
    def balance(self):
        # Pseudo root
        pr = Node(None)
        pr.right = self

        # Vine is a sorted linked list, i.e. tree with only single right children
        def treeToVine(root):
            tail = root
            rest = tail.right
            while rest:
                if not rest.left:
                    tail = rest
                    rest = rest.right
                else:
                    temp = rest.left
                    rest.left = temp.right
                    temp.right = rest
                    rest = temp
                    tail.right = temp

        def vineToTree(root, size):
            leaves = size + 1 - 2 ** math.log(size + 1, 2)

            def compress(root, count):
                scanner = root
                for i in range(int(count)):
                    child = scanner.right
                    scanner.right = child.right
                    scanner = scanner.right
                    child.right = scanner.left
                    scanner.left = child

            compress(root, leaves)
            size = size - leaves
            while size > 1:
                compress(root, size // 2)
                size = size // 2

        treeToVine(pr)
        vineToTree(pr, 8)
        return pr.right


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.right = Node(3)
root.right.right = Node(6)
root.right.left = Node(5)
root.right.left.left = Node(7)
root.right.left.right = Node(8)
root.toBST()
balanced = root.balance()
balanced.travLevelOrder()
