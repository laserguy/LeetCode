class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        global_max, global_min = nums[0], nums[0]
        curr_max, curr_min = nums[0], nums[0]

        for i in range(1,n):
            curr_max = max(curr_max+nums[i], nums[i])
            global_max = max(global_max,curr_max)

            curr_min = min(curr_min+nums[i], nums[i])
            global_min = min(global_min,curr_min)

        if global_max < 0: return global_max
        x = sum(nums) - global_min 
        return x if x > global_max else global_max