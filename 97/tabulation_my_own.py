class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)

        if len(s3) != m + n: return False

        dp = [[False]*(n+1) for _ in range(m+1)]
        
        dp[m][n] = True

        for pos1 in range(m,-1,-1):
            for pos2 in range(n,-1,-1):
                pos = pos1 + pos2
                A, B = False, False
                if pos1 < m and s3[pos] == s1[pos1]:
                    A = dp[pos1+1][pos2]
                if pos2 < n and s3[pos] == s2[pos2]:
                    B = dp[pos1][pos2+1]
                
                if pos1 + pos2 != m + n:
                    dp[pos1][pos2] = A or B
        
        print(dp)
        return dp[0][0]