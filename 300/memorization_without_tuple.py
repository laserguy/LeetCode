# DID NOT WORK: Recursive logic with memorization seems correct, runs on paper, don't know why it did not work.

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        @lru_cache(maxsize=None)
        def func(pos, last_ele = -10**10)->int:
            if pos == len(nums): return 0
            countA = func(pos+1,last_ele)
            countB = 0
            if nums[pos] > last_ele:
                countB = 1 + func(pos+1,nums[pos])
            else:
                countB = func(pos+1,nums[pos])
            
            return max(countA, countB)
        
        return func(0)