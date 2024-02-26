
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)

        @lru_cache(None)
        def func(pos: int)->int:
            if pos == n: return 0

            cost1 = costs[0] + func(pos+1)

            x = bisect.bisect_right(days,days[pos] + 7 -1)
            cost7 = costs[1] + func(x)

            x = bisect.bisect_right(days,days[pos] + 30 -1)
            cost30 = costs[2] + func(x)

            return min(cost1,min(cost7,cost30))

        return func(0)