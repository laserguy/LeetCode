class Solution:
    def numWays(self, n: int, k: int) -> int:
        def func(depth,one_back,two_back):
            count = 0
            if depth >= n: return 1

            for i in range(k):
                if i == one_back and one_back == two_back:
                    continue
                count += func(depth+1,i,one_back)

            return count

        return func(0,-1,-1)