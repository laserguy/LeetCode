class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        first_min, second_min = 101, 101

        for price in prices:
            if price < first_min:
                second_min = first_min
                first_min = price
            else:
                second_min = min(second_min,price)

        leftover = money - (first_min + second_min)
        return leftover if leftover >= 0 else money
        