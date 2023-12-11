class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        length = len(arr)

        if length == 1: return arr[0]

        count = 0

        for i in range(1,length):
            if arr[i] == arr[i-1]: count += 1
            else: count = 0

            if count >= length // 4:
                return arr[i]

        return -1