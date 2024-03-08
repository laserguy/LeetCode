class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.count = size

    def getCount(self):
        return self.count

    def find(self,x):
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX
            self.count -= 1

    def isConnected(self,x, y):
        return self.root[x] == self.root[y]

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        uf = UnionFind(n)

        for edge in edges:
            if uf.isConnected(edge[0],edge[1]):
                return False
            uf.union(edge[0],edge[1])

        return True if uf.getCount() == 1 else False