class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        # Return the possibility when n = 1
        if n == 1: return ['0','1','8']

        nums = ['0','1','6','8','9']  # possible integer that support strobogrammatic number
        
        # We only have create half of the string, other half can be created from the first half
        mid = n // 2 if n % 2 == 0 else n // 2 + 1
        half_ans = []

        """
            s: where first half of the string would be stored
            rev_s: the name here suggests it is the reverse of s, that is not completely true
                It is reverse except '6' is replaced with '9' and vice-versa
                Plus if the n is odd, then s will contain first 5 elements, then only first 4
                elements from rev_s should be taken
            depth: stop when tree reaches the half depth
        """
        def func(s: str, rev_s: str, depth: int)-> None:
            if depth == mid:
                # When depth of the tree reaches mid, combine both halves to get the string
                half_ans.append(s + rev_s[0:n//2][::-1])
                return

            for c in nums:
                if depth == 0 and c == '0': continue # The first position cannot be zero
                # In case n is odd the last depth can only contain '0','1','8'
                if depth == mid -1 and n % 2 != 0 and (c == '6' or c == '9'): continue

                # Below three lines only replaces c in case they have '6' or '9'
                char = c
                if c == '6': char = '9'
                elif c == '9': char = '6'
            
                func(s + c,rev_s + char,depth + 1)

        func("","",0)

        return half_ans