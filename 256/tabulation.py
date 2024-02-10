class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[0]*3 for _ in range(n+1)]

        for pos in range(n-1,-1,-1):
            for color in range(3):
                color1 = color + 1 if color != 2 else 0
                color2 = color - 1 if color != 0 else 2

                dp[pos][color] = min(costs[pos][color1] + dp[pos+1][color1],
                                costs[pos][color2] + dp[pos+1][color2])

        return min(dp[0])