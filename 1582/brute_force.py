class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        def isSpecial(x: int, y: int)->bool:
            for i in range(0,x):
                if mat[i][y] == 1: return False
            for i in range(x+1,m):
                if mat[i][y] == 1: return False
            for j in range(0,y):
                if mat[x][j] == 1: return False
            for j in range(y+1,n):
                if mat[x][j] == 1: return False
            return True
            
        count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and isSpecial(i,j):
                    count += 1

        return count
        