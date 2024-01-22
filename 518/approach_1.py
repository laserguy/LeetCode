class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()

        @lru_cache(maxsize=None)
        def func(sum: int, pos: int)->int:
            if pos >= n: return 0
            if sum == amount: return 1
            count = 0

            for i in range(pos,n):
                if sum + coins[i] > amount: break
                count += func(sum+coins[i], i)

            return count;

        return func(0,0)