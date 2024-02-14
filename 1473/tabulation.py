class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        dp = [[[0]*(target+2) for _ in range(n+1)] for _ in range(m+1)]

        for color in range(n+1):
            for curr_target in range(target + 2):
                if curr_target != target:
                    dp[m][color][curr_target] = 10 ** 9

        for pos in range(m+1):
            for color in range(n+1):
                dp[pos][color][target+1] = 10 ** 9

        def func()->None:
            nonlocal dp

            for pos in range(m-1,-1,-1):
                for color in range(n+1):
                    for curr_target in range(target+1):
                        if houses[pos] != 0:
                            temp = curr_target
                            if houses[pos] != color: temp += 1
                            dp[pos][color][curr_target] = dp[pos+1][houses[pos]][temp]

                        elif curr_target == target:
                            dp[pos][color][curr_target] = cost[pos][color-1] + dp[pos+1][color][target]
                        else:
                            mincost = 10 ** 9
                            for c in range(1,n+1):
                                temp = curr_target
                                if color != c: temp += 1
                                mincost = min(mincost, cost[pos][c-1] + dp[pos+1][c][temp])

                            dp[pos][color][curr_target] = mincost
            

        count = 1
        func()
        print(dp[0])
        ans = dp[0][0][0]
        if 0 in houses: return ans if ans != 10 **9 else -1
        else:
            for i in range(1,m):
                if houses[i-1] != houses[i]:
                    count += 1

        return 0 if count == target else -1

                