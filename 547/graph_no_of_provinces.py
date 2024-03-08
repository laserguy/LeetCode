class UnionFind:
    def __init__(self, size):
        self.root = [ i  for i in range(size)]

    def get_connections(self):
        return self.root

    def find(self, x):
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        UF = UnionFind(len(isConnected))

        for i in range(len(isConnected)):
            for j in range(i+1):
                if isConnected[i][j] == 1:
                    UF.union(i,j)
        
        connections = UF.get_connections()
        hash_conn = {}

        for c in connections:
            hash_conn[c] = 1

        return len(hash_conn)