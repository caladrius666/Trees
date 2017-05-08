class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


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

    def bfs_tree(self):
        Q = []
        Q.append(self.root)
        while Q:
            N = Q.pop(0)
            print(N.data, end=' ')
            if N.left:
                Q.append(N.left.root)
            if N.right:
                Q.append(N.right.root)

tree = Tree()
for x in [int(x) for x in input().split()]:
    tree.add(x)
tree.bfs_tree()
