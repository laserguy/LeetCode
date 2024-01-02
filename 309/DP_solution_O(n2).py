class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0]*(n+2)

        for i in range(n-2,-1,-1):
            C1 = 0
            for k in range(i+1,n):
                C1 = max(C1, prices[k]-prices[i]+dp[k+2])
            C2 = dp[i+1]
            dp[i] = max(C1,C2)

        return dp[0]