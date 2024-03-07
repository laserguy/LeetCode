class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)

        def fill_hash(indices: [])->dict:
            stack = []
            hash = {}
            for i in indices:
                if not stack:
                    stack.append(i)
                    continue
                
                while stack and stack[-1] <= i:
                    e = stack.pop()
                    hash[e] = i

                stack.append(i)

            while stack:
                e = stack.pop()
                hash[e] = -1
            
            return hash

        max_indices = sorted(range(n), key= lambda k:arr[k])
        min_indices = sorted(range(n), key= lambda k:arr[k], reverse=True)

        hash_max = fill_hash(max_indices)
        hash_min = fill_hash(min_indices)
 

        @lru_cache(None)
        def func(pos: int, count: bool)->bool:
            nonlocal n
            if pos == n-1: return True
            if pos == -1: return False

            p = 0
            if count == False: p = hash_max[pos]
            else: p = hash_min[pos]

            ans = func(p, not count)
            return ans

        count = 0
        for i in range(n):
            if func(i,False) == True:
                count += 1
        
        return count