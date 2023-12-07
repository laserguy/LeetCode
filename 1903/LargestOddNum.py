class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        first_odd_pos = -1
        last_odd_pos = -1
        for i in range(n-1,-1,-1):
          if first_odd_pos == -1 and int(num[i])%2 != 0:
            first_odd_pos = i

        if first_odd_pos != -1: return num[:first_odd_pos+1]
        else: return ""