class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        @lru_cache(maxsize=None)
        def func(pos: int, sum: int)->int:
            if sum == 0: return 1
            if sum < 0 or pos >= n: return 0

            count = 0

            if coins[pos] > sum:
                count += func(pos+1,sum)
            else:
                count += func(pos+1,sum) + func(pos,sum-coins[pos])

            return count

        return func(0,amount)
