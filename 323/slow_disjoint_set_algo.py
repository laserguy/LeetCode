class UnionFind:
    def __init__(self, size):
        self.root = [i for i  in range(size)]
        self.count = size

    def getCount(self):
        return self.count

    def find(self, x):
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX

            self.count -= 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for e in edges:
            uf.union(e[0],e[1])

        return uf.getCount()