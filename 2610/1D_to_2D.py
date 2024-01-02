class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        hash_map = defaultdict(int) # If key not present default value would be 0
        ans_map = defaultdict(list) # If key not present default value would be []

        for e in nums:
            ans_map[hash_map[e]].append(e)
            hash_map[e] += 1

        ans = [value for value in ans_map.values()]

        return ans