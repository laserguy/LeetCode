class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [0]*6

        for i in range(6): dp[i] = 1

        for pos in range(n-1,-1,-1):
            tmp = [0]*6
            for last_v in range(6):
                count = 0
                for v in range(1,6):
                    if last_v == 0: count += dp[v]
                    elif last_v == 1 and v == 2: count += dp[v]
                    elif last_v == 2 and (v == 1 or v == 3) : count += dp[v]
                    elif last_v == 3 and v != 3: count += dp[v]
                    elif last_v == 4 and (v == 3 or v == 5): count += dp[v]
                    elif last_v == 5 and v == 1: count += dp[v]

                tmp[last_v] = count % MOD
            dp = tmp

        return dp[0]
