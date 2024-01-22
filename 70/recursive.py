class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def func(i: int)->int:
            if i > n: return 0
            if i == n: return 1
            count = func(i+1) + func(i+2)
            return count

        return func(0)