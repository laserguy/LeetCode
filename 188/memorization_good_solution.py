class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        

        @lru_cache(None)
        def func(pos: int, buyandsell: int)-> int:
            if buyandsell > 2*k or pos >= len(prices): return 0

            do_nothing = func(pos+1,buyandsell)
            do_something = 0

            if buyandsell % 2 == 0:
                do_something = func(pos+1,buyandsell+1) - prices[pos]
            else:
                do_something = prices[pos] + func(pos+1,buyandsell+1)

            return max(do_nothing,do_something)

        return func(0,0)