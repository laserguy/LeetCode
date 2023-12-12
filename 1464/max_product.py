class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        large, second_large = 0, 0

        for e in nums:
            if e >= large:
                second_large = large
                large = e
            elif e >= second_large:
                second_large = e

        return (large-1)*(second_large-1)