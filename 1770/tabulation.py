class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)
        dp = [[0]*(m+1) for _ in range(m+1)]

        for i in range(m-1,-1,-1):
            for left in range(i,-1,-1):
                mul = multipliers[i]
                right = n-1 - (i-left)
                L = nums[left]*mul + dp[i+1][left+1]
                R = nums[right]*mul + dp[i+1][left]
                #print(f"dp[{i}][{left}] = max(dp[{i+1}][{left+1}], dp[{i+1}][{left}])  left = {left}, right = {right}")
                dp[i][left] = max(L,R)

        #print(dp)

        return dp[0][0]


        