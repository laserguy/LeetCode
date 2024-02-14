class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        n = len(costs)
        k = len(costs[0])
        dp = [0]*k

        for pos in range(n-1,-1,-1):
            tmp = [0]*k
            for color in range(k):
                tmp[color] = 10**9
                for i in range(k):
                    if i != color: # Check every color except current colot (adjacent not allowe)
                        tmp[color] = min(costs[pos][i] + dp[i],tmp[color])

            dp = tmp

        return min(dp)