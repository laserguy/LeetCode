class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        short_text, long_text = sorted([text1, text2], key=len)
        m, n = len(short_text), len(long_text)

        dp = [[0] * (n+1) for _ in range(m+1)] # (m+1) rows and (n+1) cols

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                pos = long_text.find(short_text[i],j)
                picked, not_picked = 0,0
                if pos != -1:
                    picked = 1 + dp[i+1][pos+1]
                not_picked = dp[i+1][j]

                dp[i][j] = max(picked,not_picked)

        return dp[0][0]