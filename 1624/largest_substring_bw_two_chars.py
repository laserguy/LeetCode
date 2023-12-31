class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        hash_map= {}
        max_length = -1

        for i in range(len(s)):
            if s[i] in hash_map:
                max_length = max(max_length, i- hash_map[s[i]] -1)
            else:
                hash_map[s[i]] = i


        return max_length