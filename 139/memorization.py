class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s in wordDict: return True

        max_word_size = 0
        for word in wordDict:
            if len(word) > max_word_size: max_word_size = len(word)

        @lru_cache(maxsize=None)
        def isBreakPossible(pos: int)->bool:
            for i in range(pos,len(s)):
                if len(s[pos:i+1]) > max_word_size: break
                if s[pos:i+1] in wordDict:
                    if s[i+1:] in wordDict: return True
                    else:
                        if isBreakPossible(i+1) == True: return True
            return False

        return isBreakPossible(0)