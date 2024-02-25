class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        max_len = 0

        @lru_cache(None)
        def func(pos1: int, pos2: int, count: int)->None:
            nonlocal max_len
            max_len = max(max_len,count)
            if pos1 == n1 or pos2 == n2:
                return 0

            func(pos1 + 1, pos2, 0)
            func(pos1, pos2 + 1, 0)

            if nums1[pos1] == nums2[pos2]:
                func(pos1 + 1, pos2 + 1, count + 1)

        func(0,0,0)
        return max_len
        