import math

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        """
            1 - Write the framework
            2 - Find the search space
            3 - Write the condition function
        """
        a, b, c = sorted([a,b,c])
        """
            # STEP 3: 
            Monotonicity is very important to apply Binary search, that means
            When condition(value) is True => then condition(value+1) is also True
            Here in this case we are checking if:
                condition(value) has n numbers <= 'value' => if true
                Then definitely value+1 will have n numbers smaller that it
              
        """
        def condition(value) -> bool:
            count_a, count_b, count_c = value // a, value // b, value // c
            count_ab = value // (a*b // math.gcd(a,b))
            count_bc = value // (b*c // math.gcd(b,c))
            count_ac = value // (a*c // math.gcd(a,c))

            if b >= a and b % a == 0:
                count_b, count_ab, count_bc = 0, 0, 0
            if c >= a and c % a == 0:
                count_c, count_ac, count_bc = 0, 0, 0
            if c >= b and c % b == 0:
                count_c, count_bc, count_ac = 0, 0, 0
            
            total_count = count_a + count_b + count_c
            duplicate_count = count_ab + count_bc + count_ac

            count = total_count - duplicate_count
            return count >= n
        """
        # STEP 2: 
            Binary search can only work when there is a increasing search space
            And the search space should cover all the elements in the search space
        """
        low, high = min(min(a,b),c), n*a*b*c
        # STEP 1:
        while low < high:
            mid = low + (high-low) // 2
            if condition(mid):
                high = mid
            else:
                low = mid+1
        return low