class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*(2*k+1) for _ in range(n+1)]

        for pos in range(n-1,-1,-1):
            for buyandsell in range(2*k-1,-1,-1):
                do_nothing = dp[pos+1][buyandsell]
                do_something = 0

                if buyandsell % 2 == 0:
                    do_something = dp[pos+1][buyandsell+1] - prices[pos]
                else:
                    do_something = dp[pos+1][buyandsell+1] + prices[pos]
                
                dp[pos][buyandsell] = max(do_nothing,do_something)

        return dp[0][0]