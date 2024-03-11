from collections import defaultdict

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_dict = defaultdict(int)

        for c in s:
            s_dict[c] += 1

        out = ""
        for c in order:
            out += c * s_dict[c]
            s_dict[c] = 0

        for key in s_dict:
            out += key * s_dict[key]

        return out