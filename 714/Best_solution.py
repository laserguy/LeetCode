class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        
        held_prev, nheld_prev = float('-inf'), 0

        for price in prices:
            held = max(-price - fee + nheld_prev, held_prev)
            nheld = max(price + held_prev, nheld_prev)

            held_prev, nheld_prev = held, nheld

        return max(held_prev, nheld_prev)