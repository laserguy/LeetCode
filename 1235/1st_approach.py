from sortedcontainers import SortedDict

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        dp = [0]*(max(endTime)+1)
        hash_map = SortedDict()

        for i in range(len(endTime)):
            if endTime[i] not in hash_map:
                hash_map[endTime[i]] = []
            hash_map[endTime[i]].append((startTime[i],profit[i]))

        for key in range(1,len(dp)):
            if key in hash_map:
                for value in hash_map[key]:
                    temp = dp[value[0]] + value[1]
                    dp[key] = max(dp[key],temp)
            dp[key] = max(dp[key],dp[key-1])

        return max(dp)