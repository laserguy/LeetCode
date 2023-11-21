class Solution:
    def minFallingPathSum(self, a: List[List[int]]) -> int:
        matrix_rows = len(a)
        matrix_cols = len(a[0])

        for i in range(1,matrix_rows):
            for j in range(matrix_cols):
                minim = a[i][j] + a[i-1][j]
                if j > 0:
                    temp = a[i][j] + a[i-1][j-1]
                    minim = temp if temp < minim else minim
                if j < matrix_cols-1:
                    temp = a[i][j] + a[i-1][j+1]
                    minim = temp if temp < minim else minim
                a[i][j] = minim

        return min(a[matrix_rows-1])