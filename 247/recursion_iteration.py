class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n == 1: return ['0','1','8']

        nums = ['0','1','6','8','9']
        mid = n // 2 if n % 2 == 0 else n // 2 + 1
        half_ans = []

        def func(s: str, depth: int)-> None:
            if depth == mid:
                half_ans.append(s)
                return

            for c in nums:
                if depth == 0 and c == '0': continue
                if depth == mid -1 and n % 2 != 0 and (c == '6' or c == '9'): continue

                temp = s + c
                func(temp,depth + 1)

        func("",0)
        
        # The difference with complete recurive approach and this one is:
        # Complete recusion is faster as we calculate the reverse side at the same time and append during recursion
        # Here it is done separately
        for i in range(len(half_ans)):
            s = half_ans[i][0:n//2]
            temp = ''
            for c in s:
                if c == '6': temp += '9'
                elif c == '9': temp += '6'
                else: temp += c

            temp = temp[::-1]
            half_ans[i] += temp

        return half_ans