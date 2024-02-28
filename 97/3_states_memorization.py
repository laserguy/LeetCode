class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)

        if len(s3) != m + n: return False

        @lru_cache(None)
        def func(pos3: int, pos1: int, pos2: int)->bool:
            if pos3 == m + n: return True

            A, B = False, False
            if pos1 < m and s3[pos3] == s1[pos1]:
                A =  func(pos3+1,pos1+1,pos2)

            if pos2 < n and s3[pos3] == s2[pos2]:
                B = func(pos3+1,pos1,pos2+1)

            return A or B

        return func(0,0,0)