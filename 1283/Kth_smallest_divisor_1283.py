class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        """
            1 - Write the framework
            2 - Find the search space
            3 - Write the condition function
        """
        """
            # STEP 3: 
            Monotonicity is very important to apply Binary search, that means
            When condition(value) is True => then condition(value+1) is also True
            condition(value) returns True if summation is less than equal to threshold for that 'value'
            If it is True for 'value', then we can see it will be True foe 'value+1' as well
            Check example 1: True for 5, it is definelty True for 6 => monotonicity
              
        """
        def condition(value) -> bool:
            ceildev = lambda a, b: -(-a//b)
            sum = 0
            for num in nums:
                sum += ceildev(num, value)

            return sum <= threshold
        
        """
        # STEP 2: 
            Binary search can only work when there is a increasing search space
            And the search space should cover all the elements in the search space
        """
        low, high = 1, max(nums)
        # STEP 1:
        while low < high:
            mid = low + (high-low) // 2
            if condition(mid):
                high = mid
            else:
                low = mid + 1
        
        return low