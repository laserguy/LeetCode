class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10 ** 9 + 7
        ROWS, COLS = m, n
        dp = [[0]*COLS for _ in range(ROWS)]

        for depth in range(maxMove):
            tmp = [[0]*COLS for _ in range(ROWS)]

            for r in range(ROWS):
                for c in range(COLS):
                    if r + 1 ==  ROWS: tmp[r][c] += 1
                    else: tmp[r][c] += dp[r+1][c]

                    if r - 1 < 0: tmp[r][c] += 1
                    else: tmp[r][c] += dp[r-1][c]

                    if c + 1 ==  COLS: tmp[r][c] += 1
                    else: tmp[r][c] += dp[r][c+1]

                    if c - 1 <  0: tmp[r][c] += 1
                    else: tmp[r][c] += dp[r][c-1]
            dp = tmp
        
        return dp[startRow][startColumn] % MOD