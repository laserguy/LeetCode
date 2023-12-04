class Solution:
    def maximalSquare(self, dp: List[List[str]]) -> int:
        max_square = 0
        m, n = len(dp), len(dp[0])

        if m == 0: return 0
        if "1" in dp[0]: max_square = 1
        for i in range(m):
            if dp[i][0] == "1":
                max_square = 1
                break

        for i in range(1,m):
            for j in range(1,n):
                count = 0
                if dp[i][j] == "1":
                    if dp[i-1][j-1] == "0":
                        dp[i][j] = "1"
                        count = 1
                    else:
                        if int(dp[i-1][j]) >= int(dp[i-1][j-1]) and int(dp[i][j-1]) >= int(dp[i-1][j-1]):
                            count = int("1") + int(dp[i-1][j-1])
                            dp[i][j] = str(count)
                        else:
                            count = min(int(dp[i-1][j]),int(dp[i][j-1])) + 1
                            dp[i][j] = str(count)
                max_square = count if count > max_square else max_square

        print(dp)
        return max_square*max_square
