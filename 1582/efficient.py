class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        I, J = {}, {}
            
        count = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    I[i] = I.get(i,0)+1
                    J[j] = J.get(j,0)+1

        count = 0
        for i in I.keys():
            if I[i] == 1:
                for j in J.keys():
                    if J[j] == 1:
                        if mat[i][j] == 1:
                            count += 1

        return count
        