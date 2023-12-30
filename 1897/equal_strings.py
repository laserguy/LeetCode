class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        total_length = 0
        hash_map = {}
        
        for word in words:
            total_length += len(word)
            for c in word:
                hash_map[c] = hash_map.get(c,0)+1

        if total_length % len(words) != 0: return False
        if len(hash_map) > (total_length // len(words)): return False

        for c in hash_map:
            if hash_map[c] % len(words) != 0: return False

        return True