class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7
        
        @lru_cache(None)
        def func(i: int, j: int, depth: int)->int:
            if depth > maxMove: return 0
            if i >= m or j >= n or i < 0 or j < 0:
                return 1
            
            A = func(i+1,j,depth+1)
            B = func(i-1,j,depth+1)
            C = func(i,j+1,depth+1)
            D = func(i,j-1,depth+1)

            return (A + B + C + D)

        count = func(startRow,startColumn,0)
        return count% MOD