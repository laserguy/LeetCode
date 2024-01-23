class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0]*n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] != 1: dp[i][0] = 1
            else: break
        for i in range(n):
            if obstacleGrid[0][i] != 1: dp[0][i] = 1
            else: break

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]