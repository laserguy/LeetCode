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

        print(hash_max)
        print(hash_min)
 
        total = 1
        for i in range(n-2,-1,-1):
            pos = i
            odd = True
            while pos != n-1 and pos != -1:
                if odd: pos = hash_max[pos]
                else: pos = hash_min[pos]
                odd = not odd
            if pos == n-1:
                print(i)
                total += 1
        
        return total
