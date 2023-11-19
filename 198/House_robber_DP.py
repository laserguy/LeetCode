class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        DP = [0]*length
        DP[0] = nums[0]
        """
            To build our DP tabulation, at each step we have to figure out what would be maximum money at that stage. At each step the maximum money possible is max(F(n-1),F[n-2]+nums[n])
        """
        for i in range(1,length):
            DP[i] = max(
                DP[i-1],
                (DP[i-2] if i>=2 else 0) + nums[i]
            )
        print(DP)
        return DP[length-1]
