# Solution did not work: Becuase 'Output Limit was exceeded', at one point the key for the LRU cache became very huge as whole tuple is stored here

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        max_length = -1

        @lru_cache(maxsize=None)
        def func(pos, out=()):
            nonlocal max_length
            if len(out) > max_length: max_length = len(out)
            print(out)
            if pos == len(nums): return
            if len(out) == 0:
                func(pos+1, out + (nums[pos],))
            else:
                func(pos+1, out)
                if nums[pos] > out[-1]:
                    func(pos+1, out + (nums[pos],))
                else:
                    func(pos+1, (nums[pos],))

        func(0)
        return max_length