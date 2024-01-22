class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0]*(amount+1)
        dp[0] = 1

        for pos in range(n-1,-1,-1):
            for sum in range(coins[pos],amount+1):
                dp[sum] += dp[sum-coins[pos]]

        return dp[amount]