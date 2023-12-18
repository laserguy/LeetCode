class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sL, tL = len(s), len(t)

        if sL != tL: return False

        sum_s, mul_s = 0, 1
        sum_t, mul_t = 0, 1

        for c_s, c_t in zip(s,t):
            sum_s += ord(c_s)
            sum_t += ord(c_t)
            mul_s *= ord(c_s)
            mul_t *= ord(c_t)

        if sum_s == sum_t and mul_s == mul_t:
            return True
        
        return False