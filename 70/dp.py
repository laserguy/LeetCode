class Solution:
    def climbStairs(self, n: int) -> int:
        one_back, two_back = 2, 1
        pos = 3

        while(pos <= n):
            curr = one_back + two_back
            two_back = one_back
            one_back = curr
            pos += 1

        return one_back if n >= 2 else two_back