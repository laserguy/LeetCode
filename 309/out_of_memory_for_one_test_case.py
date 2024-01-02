class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @lru_cache(None)
        def func(pos: int, buyandsell: int, cooldown: bool)-> int:
            if pos >= len(prices): return 0

            do_nothing = func(pos+1,buyandsell,False)
            if cooldown == True: return do_nothing

            do_something = 0

            if buyandsell % 2 == 0:
                do_something = func(pos+1,buyandsell+1,False) - prices[pos]
            else:
                do_something = prices[pos] + func(pos+1,buyandsell+1,True)

            return max(do_nothing,do_something)

        return func(0,0,False)