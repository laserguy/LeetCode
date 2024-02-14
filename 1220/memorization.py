class Solution:
    def countVowelPermutation(self, n: int) -> int:
        vowels = ['a','e','i','o','u']
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def func(pos: int, last_v: int)->int:
            nonlocal vowels
            if pos == n: return 1
            count = 0

            for v in vowels:
                if last_v =='': count += func(pos+1,v)
                elif last_v == 'a' and v == 'e': count += func(pos+1,v)
                elif last_v == 'e' and (v == 'a' or v == 'i'): count += func(pos+1,v)
                elif last_v == 'i' and v != 'i': count += func(pos+1,v)
                elif last_v == 'o' and (v == 'i' or v == 'u'): count += func(pos+1,v)
                elif last_v == 'u' and v == 'a': count += func(pos+1,v)

            return count % MOD

        return func(0,'')