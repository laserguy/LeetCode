class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1: return k
        two_back, one_back = k, k*k

        for i in range(2,n):
            current = (k-1)*(one_back + two_back)
            two_back = one_back
            one_back = current

        return one_back