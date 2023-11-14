class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        """
            1 - Write the framework
            2 - Find the search space
            3 - Write the condition function
        """
        """
        # STEP 3: 
            Monotonicity is very important to apply Binary search, that means
            When condition(value) is True => then condition(value+1) is also True
            Here in this case we are checking if:
                condition(value) has k numbers less value => if true
                Then definitely value+1 will have k numbers smaller that it
                Therefore monotonicity is satisfied
        """
        def condition(value) -> bool:
            count = 0
            """
                We have to count how many numbers are less than 'value'
                The calculation is done row-wise below.
            """
            for row in range(1,m+1):
                add = min(value//row,n)
                if add == 0: break
                count += add
            
            return count >= k
            
        """
        # STEP 2: 
            Binary search can only work when there is a increasing search space
            And the search space should cover all the elements in the search space
        """
        low, high = 1, m*n

        # STEP: 1
        while low < high:
            mid = low + (high-low) // 2
            if condition(mid):
                high = mid
            else:
                low = mid + 1

        return low
