from collections import defaultdict

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        
        sorted_zipped_list = sorted(zip(startTime, endTime, profit))
        startTime, endTime, profit = zip(*sorted_zipped_list)
        
        @lru_cache(maxsize=None)
        def func(pos: int, start: int, end: int)->int:
            if pos >= n: return 0

            p1 = 0
            if startTime[pos] >= end:
                p1 = profit[pos] + func(pos+1, startTime[pos], endTime[pos]) 

            p2 = func(pos+1, start, end)

            return max(p1,p2)

        return func(0,-1,-1)