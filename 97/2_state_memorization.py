class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)

        if len(s3) != m + n: return False

        @lru_cache(None)
        def func(pos1: int, pos2: int)->bool:
            pos = pos1 + pos2
            if pos == m + n: return True

            A, B = False, False
            if pos1 < m and s3[pos] == s1[pos1]:
                A =  func(pos1+1,pos2)

            if pos2 < n and s3[pos] == s2[pos2]:
                B = func(pos1,pos2+1)

            return A or B

        return func(0,0)