class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1

        for pos in range(n-1,-1,-1):
            for sum in range(1,amount+1):
                if coins[pos] > sum:
                    dp[pos][sum] += dp[pos+1][sum]
                else:
                    dp[pos][sum] += dp[pos+1][sum] + dp[pos][sum-coins[pos]]

        return dp[0][amount]
