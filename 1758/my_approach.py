class Solution:
    def minOperations(self, s: str) -> int:
        start_with_zero = 0 # operations required when started with zero
        start_with_one = 0  # operations required when started with one

        for i in range(len(s)):
            if i%2 == 0: # even positions
                if s[i] == '0':
                    start_with_one += 1
                else: start_with_zero += 1
            else: # odd positions
                if s[i] == '1': start_with_one += 1
                else: start_with_zero += 1

        print(start_with_zero,start_with_one)
        return min(start_with_zero,start_with_one)