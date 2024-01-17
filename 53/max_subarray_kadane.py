class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev_sum, max_sum = nums[0], nums[0]
        n = len(nums)

        for i in range(1,n*2):
            if prev_sum < 0: prev_sum = nums[i%n]
            else: prev_sum += nums[i%n]

            if prev_sum > max_sum : max_sum = prev_sum

        return max_sum