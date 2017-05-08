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

    def height(self, deeps, h):
        if self.root:
            if self.root.left:
                self.root.left.height(deeps, h+1)
                if self.root.right:
                    self.root.right.height(deeps, h+1)
            elif self.root.right:
                self.root.right.height(deeps, h+1)
                if self.root.left:
                    self.root.left.height(deeps, h+1)
            else:
                deeps.append(h)
        return max(deeps)

    def print(self, flag='YES'):
        if self.root:
            if self.root.left and not self.root.right:
                if self.root.left.height([], 1) > 1:
                    flag = 'NO'
                self.root.left.print(flag)
            if self.root.right and not self.root.left:
                if self.root.right.height([], 1) > 1:
                    flag = 'NO'
                self.root.right.print(flag)
            if self.root.right and self.root.left:
                if abs(self.root.right.height([], 1) - self.root.left.height([], 1)) > 1:
                    flag = 'NO'
        return flag

tree = Tree()
for x in [int(x) for x in input().split()]:
    tree.add(x)
print(tree.print())
