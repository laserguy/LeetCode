class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7
        n = len(arr)
        min_sum = 0
        stack = []

        for i in range(n+1):
            while stack and (i == n or arr[stack[-1]] >= arr[i]):
                idx = stack.pop()
                left = -1 if not stack else stack[-1]
                min_sum += arr[idx]*(i-idx)*(idx-left)

            stack.append(i)

        return min_sum%MOD
