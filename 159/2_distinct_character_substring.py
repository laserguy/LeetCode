class Solution:
    """
        For most substring problem, we are given a string and need to find a substring
        of it which satisfy some restrictions. A general way is to use a hashmap
        assisted with two pointers. The template is given below.
    """
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        count_map = [0]*128
        
        start, end = 0, 0
        max_length = -1

        counter = 0
        
        while end < len(s):
            if count_map[ord(s[end])] == 0: 
                counter += 1
            count_map[ord(s[end])] += 1
            end += 1
            
            # When condition is valid, update the answer
            if counter <= 2:
                if end-start > max_length:
                    max_length = end - start

            # while condition remains invalid, keep incrementing 'start' until it becomes valid again
            while counter > 2:
                count_map[ord(s[start])] -= 1
                if count_map[ord(s[start])] == 0:
                    counter -= 1
                start += 1
        
        return max_length if max_length != -1 else 0    