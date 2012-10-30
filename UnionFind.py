class Node:
    def __init__(self, label):
        self.parent = self
        self.rank = 0
        self.size = 1
        self.label = label
    def __repr__(self):
        return self.label

class UnionFind:
    def __init__(self):
        self.items = {}

    def get(self,x):
        if not self.items.has_key(x):
            self.items[x] = Node(x)
        return self.items[x]

    def find(self,x):
        if not isinstance(x,Node):
            x = self.get(x)
        
        if x.parent is not x:
            x.parent = self.find(x.parent)
            
        return x.parent

    def union(self,x,y):
        x = self.get(x)
        y = self.get(y)
        
        xRoot = self.find(x)
        yRoot = self.find(y)
        if xRoot is yRoot:
            return
        
        if xRoot.rank < yRoot.rank:
            xRoot.parent = yRoot
            yRoot.size += xRoot.size

        elif yRoot.rank < xRoot.rank:
            yRoot.parent = xRoot
            xRoot.size += yRoot.size

        else:
            yRoot.parent = xRoot
            xRoot.size += yRoot.size
            xRoot.rank += 1

    def getSize(self,x):
        x = self.get(x)
        x = self.find(x)
        return x.size
