
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [0]*(n+1)

        for pos in range(n-1,-1,-1):
            cost1 = costs[0] + dp[pos + 1]
            x = bisect.bisect_right(days,days[pos] + 7 - 1)
            cost7 = costs[1] + dp[x]
            x = bisect.bisect_right(days,days[pos] + 30 - 1)
            cost30 = costs[2] + dp[x]

            dp[pos] = min(cost1,min(cost7,cost30))

        return dp[0]