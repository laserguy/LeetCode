import sys

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        """
            1 - Write the framework
            2 - Find the search space
            3 - Write the condition function
        """
        nums.sort()
        """
            # STEP 3: 
            Monotonicity is very important to apply Binary search, that means
            When condition(value) is True => then condition(value+1) is also True
            Here in this case we are checking if:
                condition(value) has k numbers <= 'value' => if true
                Then definitely value+1 will have k numbers smaller that it
              
        """
        def condition(value) -> bool:
            # Using two pointer approach to solve the problem
            fast, slow = 0, 0
            count = 0
            length = len(nums)
            while slow < length or fast < length:
                while fast < length and (nums[fast]-nums[slow]) <= value:
                    fast += 1
                # Number of elements less than value would be the difference of fast and slow
                count += fast-slow-1
                slow += 1
            return count >= k

        """
        # STEP 2: 
            Binary search can only work when there is a increasing search space
            And the search space should cover all the elements in the search space
        """
        low, high = 0, max(nums)-min(nums)
        # STEP 1:
        while low < high:
            mid = low + (high-low) // 2
            if condition(mid):
                high = mid
            else:
                low = mid+1

        return low