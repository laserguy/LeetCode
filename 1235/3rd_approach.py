from collections import defaultdict

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        dp = [0]*(n+1)

        sorted_zipped_list = sorted(zip(startTime, endTime, profit))
        startTime, endTime, profit = zip(*sorted_zipped_list)
        
        for pos in range(n-1,-1,-1):
            nextindex = pos + bisect.bisect_left(startTime[pos:], endTime[pos])
            p1 = profit[pos] + dp[nextindex]
            p2 = dp[pos+1]
            dp[pos] = max(p1,p2)

        return dp[0]