class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        @lru_cache(None)
        def func(pos: int, color: int, curr_target: int)->int:
            if pos >= m and curr_target != target: return 10 ** 9
            if pos >= m: return 0
            if curr_target > target: return 10 ** 9
            
            if houses[pos] != 0:
                if houses[pos] != color: curr_target += 1
                return func(pos+1,houses[pos], curr_target)

            if curr_target == target:
                return cost[pos][color-1] + func(pos+1,color,target)

            mincost = 10**9
            for c in range(1,n+1):
                if color != c:
                    mincost = min(mincost, cost[pos][c-1] + func(pos+1,c,curr_target+1))
                else:
                    mincost = min(mincost, cost[pos][c-1] + func(pos+1,c,curr_target))

            return mincost

        count = 1
        ans = func(0,0,0)
        if 0 in houses: return ans if ans != 10 **9 else -1
        else:
            for i in range(1,m):
                if houses[i-1] != houses[i]:
                    count += 1

        return 0 if count == target else -1

                