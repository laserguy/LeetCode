class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        short_text, long_text = sorted([text1, text2], key=len)
        max_length = 0
        #print(short_text, long_text)

        @lru_cache(maxsize=None)
        def dp(short_pos, long_pos) -> str:
            if short_pos == len(short_text) or long_pos == len(long_text):
                return ""

            pos = long_text.find(short_text[short_pos],long_pos)

            picked, not_picked = "", ""
            if pos != -1:
                picked = short_text[short_pos] + dp(short_pos+1,pos+1)
            not_picked = dp(short_pos+1,long_pos)
            return picked if len(picked) > len(not_picked) else not_picked

        out = dp(0,0)
        
        return len(out)