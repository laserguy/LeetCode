
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}

        def func(days_index):
            if days_index == len(days): return 0
            if days_index in dp: return dp[days_index]

            dp[days_index] = 10**10

            for d,cost in zip([1,7,30],costs):
                j = days_index
                while j < len(days) and days[j] < days[days_index] + d:
                    j += 1
                dp[days_index] = min(dp[days_index],cost + func(j))

            return dp[days_index]
        
        return func(0)