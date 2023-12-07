class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d: return -1

        dp = [[0]*(d+1) for _ in range(n+1)]
        hardest = 0
        for i in range(n-1,-1,-1):
            hardest = max(hardest,jobDifficulty[i])
            dp[i][d] = hardest

        for i in range(n,-1,-1):
            for j in range(n-(d-day)-1,-1,-1)

        return dp[0][1]