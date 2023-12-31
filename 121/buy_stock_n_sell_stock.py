class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_right, max_profit = -1, 0

        for i in range(len(prices)-1,-1,-1):
            if max_right > prices[i]:
                max_profit = max(max_profit,max_right-prices[i])
            else:
                max_right = prices[i]

        return max_profit