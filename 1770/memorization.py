class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        @lru_cache
        def dp(start, end, pos):
            if pos == len(multipliers): return 0

            left = nums[start]*multipliers[pos] + dp(start+1,end,pos+1)

            if start == end: return left

            right = nums[end]*multipliers[pos] + dp(start,end-1,pos+1)
            
            return max(left,right)

        start, end = 0, len(nums)-1

        return dp(start,end,0)