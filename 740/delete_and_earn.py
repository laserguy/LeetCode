class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        length = len(nums)

        # sort, count and put in map
        nums.sort()
        count = 1
        count_map = {}
        count_map[nums[0]] = 1
        for i in range(1,length):
            if nums[i] == nums[i-1]:
                count += 1
                if i == length-1: count_map[nums[i]] = count
            else:
                count_map[nums[i-1]] = count
                count = 1
                count_map[nums[i]] = 1
        print(count_map)

        # create a DP array
        distinct_nums = list(count_map.keys())
        print(distinct_nums)
        distinct_length = len(distinct_nums)
        dp = [0]*distinct_length
        dp[0] = distinct_nums[0]*count_map[distinct_nums[0]]
        if distinct_length == 1: return dp[0]

        temp = distinct_nums[1]*count_map[distinct_nums[1]]
        dp[1] = temp if distinct_nums[1]-1 == distinct_nums[0] else dp[0]+temp
        dp[1] = max(dp[0],dp[1])

        for i in range(2, distinct_length):
            if distinct_nums[i]-1 != distinct_nums[i-1]:
                dp[i] = dp[i-1] + count_map[distinct_nums[i]]*distinct_nums[i]
            else:
                dp[i] = dp[i-2] + count_map[distinct_nums[i]]*distinct_nums[i]
            dp[i] = max(dp[i],dp[i-1])
        print(dp)
        return max(dp[distinct_length-1],dp[distinct_length-2])