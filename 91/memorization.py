class Solution:
    def numDecodings(self, s: str) -> int:
        length = len(s)

        @lru_cache(maxsize=None)
        def func(pos: int) -> int:
            count = 0
            if pos == length:
                return 1
            if s[pos] == '0': return 0

            count += func(pos+1)

            if pos != length-1 and int(s[pos]) <= 2:
                num = int(s[pos])*10 + int(s[pos+1])
                if num <=26:
                    count += func(pos+2)

            return count
        
        return func(0)