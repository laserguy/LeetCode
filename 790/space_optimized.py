class Solution:
    def numTilings(self, n: int) -> int:
        fc_two_back, fc_one_back = 1, 2   # fc : short for 'fully covered'
        pc_one_back = 1                   # pc : short for 'partially covered'
        MOD = 10**9 + 7

        # 'fc' and 'pc' stores the current value(i) of the fully and partially covered
        for i in range(2,n):
            fc = (fc_one_back + fc_two_back + 2*pc_one_back) % MOD
            pc = (pc_one_back + fc_two_back) % MOD

            fc_two_back, fc_one_back = fc_one_back, fc
            pc_one_back = pc

        return fc_one_back if n > 1 else fc_two_back
            