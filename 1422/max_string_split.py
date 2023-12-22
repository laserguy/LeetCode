class Solution:
    def maxScore(self, s: str) -> int:
        zeros, ones = 0, 0

        for c in s:
            if c == '1': ones += 1

        max_score = -1

        for i in range(len(s)-1):
            if s[i] == '0':
                zeros += 1
            else: ones -= 1

            score = ones + zeros
            if score > max_score:
                max_score = score

        return max_score