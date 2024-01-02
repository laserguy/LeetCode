class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pre_sold = float('-inf')
        held, sold, rest = float('-inf'), float('-inf'), 0

        for price in prices:
            pre_sold = sold
            sold = held + price
            held = max(held,rest-price)
            rest = max(pre_sold,rest)

        return max(sold,rest)