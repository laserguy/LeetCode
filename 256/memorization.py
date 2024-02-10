class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        @lru_cache(None)
        def func(pos: int, state: str)->int:
            if pos >= n: return 0
            cost = 0

            if state == 'R':
                cost = min(costs[pos][1] + func(pos+1, 'B'),
                        costs[pos][2] + func(pos+1,'G'))

            elif state == 'G':
                cost = min(costs[pos][0] + func(pos+1, 'R'),
                        costs[pos][1] + func(pos+1,'B'))

            elif state == 'B':
                cost = min(costs[pos][0] + func(pos+1, 'R'),
                        costs[pos][2] + func(pos+1,'G'))

            else:
                temp = min(costs[pos][0] + func(pos+1, 'R'),
                        costs[pos][1] + func(pos+1,'B'))
                cost = min(temp, costs[pos][2] + func(pos+1,'G'))

            return cost

        return func(0,'')