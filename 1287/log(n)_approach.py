# Binary search method

"""
Let's continue thinking about the array being split into blocks of similar elements. The answer block has a length greater than n / 4, and thus it must overlap at least one of the following positions in the array:

A quarter of the way through at index n / 4.
Halfway through at index n / 2.
Three-quarters of the way through at index 3n / 4.

We will only consider the elements at each of these indices as candidates since one of them must be the answer. For a given candidate, we can find its frequency by identifying its block size. To identify its block size, we find the leftmost index in which candidate appears as left and the rightmost index in which candidate appears as right. Then, the size of the block is right - left + 1. We can calculate left and right using binary search.

"""

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        N = len(arr)

        positions = [N//4, (2*N)//4, (3*N)//4] 
        max_diff = 0
        output = -1

        for pos in positions:
            left = bisect.bisect_left(arr,arr[pos])
            right = bisect.bisect_right(arr,arr[pos])-1
            if right-left+1 > N/4:
                return arr[pos]

        return -1
                
