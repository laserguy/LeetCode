import sys

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        length = len(coins)
        DP = [sys.maxsize]*(amount+1)
        DP[0] = 0

        for j in range(1,amount+1):
            for i in range(length):
                if coins[i] > j : break
                DP[j] = min(
                    DP[j],
                    DP[j - coins[i]] + 1
                )

        print(DP)
        return -1 if DP[amount] == sys.maxsize else DP[amount]