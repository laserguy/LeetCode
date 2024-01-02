class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        held = [float('-inf')]*(n+1)
        sold = [float('-inf')]*(n+1)
        rest = [0]*(n+1)

        for i in range(n):
            held[i] = max(held[i-1],rest[i-1]-prices[i])
            sold[i] = held[i-1] + prices[i]
            rest[i] = max(sold[i-1],rest[i-1])

        return max(sold[n-1],rest[n-1])