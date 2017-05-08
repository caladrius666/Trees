class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.freq = 1


class Tree:
    def __init__(self):
        self.root = None

    def add(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            if data > self.root.data:
                if not self.root.right:
                    self.root.right = Tree()
                    self.root.right.add(data)
                else:
                    self.root.right.add(data)
            if data < self.root.data:
                if not self.root.left:
                    self.root.left = Tree()
                    self.root.left.add(data)
                else:
                    self.root.left.add(data)
            if data == self.root.data:
                self.root.freq += 1

    def print(self):
        if self.root:
            if self.root.left:
                self.root.left.print()
            print(self.root.data, self.root.freq)
            if self.root.right:
                self.root.right.print()

tree = Tree()
for x in [int(x) for x in input().split()]:
    tree.add(x)
tree.print()
