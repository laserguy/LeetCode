class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        hashmap = {}

        for c_s, c_t in zip(s,t):
            hashmap[c_s] = hashmap.get(c_s,0)+1
            hashmap[c_t] = hashmap.get(c_t,0)-1

        for key in hashmap.keys():
            if hashmap[key] != 0:
                return False

        return True