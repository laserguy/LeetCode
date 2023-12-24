class Solution:
    def minOperations(self, s: str) -> int:
        start_with_zero = 0 # operations required when started with zero

        for i in range(len(s)):
            if i%2 == 0: # even positions
                if s[i] == '1':
                    start_with_zero += 1
            else: # odd positions
                if s[i] == '0':
                    start_with_zero += 1

        print(start_with_zero,len(s)-start_with_zero)
        return min(start_with_zero,len(s)-start_with_zero)