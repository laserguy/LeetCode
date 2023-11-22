import math

class Solution:
    def minSteps(self, n: int) -> int:
        def isPrime(num: int) -> bool:
            if num <= 3 and num > 0: return True
            i = 2
            while i < math.sqrt(num) + 1: 
                if num%i == 0: return False
                i+=1
            
            return True

        dp = [0]*n
        dp[0] = 0

        for i in range(1,n):
            if isPrime(i+1): dp[i] = i+1

        for i in range(2,n//2+1):
            j = 2
            while i*j <= n:
                dp[i*j-1] = dp[i-1] + 1 + (j-1)
                j +=1

        return dp[n-1]