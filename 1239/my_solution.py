class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        max_len = 0
        @lru_cache(None)
        def func(pos: int, s: str)->None:
            nonlocal max_len
            max_len = max(len(s),max_len)
            if pos >= n: return
            if len(arr[pos]) != len(set(arr[pos])):
                func(pos + 1, s)
                return

            # Does 's' and string at current position have anything in common
            if not (set(s) & set(arr[pos])):
                func(pos + 1, s + arr[pos])
            func(pos + 1, s)

        func(0,"")
        return max_len