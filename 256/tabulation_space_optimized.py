class Solution:
    # space optimized
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [0]*3

        for pos in range(n-1,-1,-1):
            tmp = [0]*3
            for color in range(3):
                color1 = color + 1 if color != 2 else 0
                color2 = color - 1 if color != 0 else 2

                tmp[color] = min(costs[pos][color1] + dp[color1],
                                costs[pos][color2] + dp[color2])

            dp = tmp

        return min(dp)