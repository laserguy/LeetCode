class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        start, end = 0, 0
        counter = 0
        hashmap = {}
        max_fruits = 0

        for end in range(len(fruits)):
            if counter <=2:
                if fruits[end] in hashmap:
                    if hashmap[fruits[end]] == 0: counter += 1
                    hashmap[fruits[end]] += 1
                else:
                    counter +=1
                    hashmap[fruits[end]] =1
            #print(hashmap, counter, start, end, max_fruits)
            if counter == 2:
                max_fruits = end-start+1 if (end-start+1) > max_fruits else max_fruits

            while counter > 2:
                if (end-start) > max_fruits:
                    max_fruits = end-start
                    print(fruits[end],fruits[start],end,start)

                hashmap[fruits[start]] -= 1
                if hashmap[fruits[start]] == 0: counter -= 1
                start += 1

        if max_fruits == 0: return hashmap[fruits[0]]

        return max_fruits