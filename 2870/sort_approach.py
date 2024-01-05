class Solution:
    def minOperations(self, nums: List[int]) -> int:
        slow, fast, ops = 0, 1, 0
        nums.sort()

        def calculate_ops(count: int) -> int:
            if count == 1: return -1
            elif count == 2: return 1
            else:
                if count % 3 == 0: return count // 3
                else: return count // 3 + 1
            
            return 0

        while fast < len(nums):
            if nums[slow] != nums[fast]:
                count = fast - slow
                if calculate_ops(count) == -1: return -1
                else: ops += calculate_ops(count)
                slow = fast

            fast += 1


        remain = calculate_ops(fast-slow)
        if remain == -1: return -1
        return ops + remain