class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
            For most substring problem, we are given a string and need to find a substring
            of it which satisfy some restrictions. A general way is to use a hashmap
            assisted with two pointers. The template is given below.
        """
        count_map = [0]*128  # List which will act as a count map
        
        for e in t:
            # Do some inital required operation in the map
            # Here setting each element of 't' as key in map and asigning it to 1
            count_map[ord(e)] += 1

        counter = len(t)   # To check substring is valid
        start, current = 0, 0  # Two pointers
        min_length = float('inf')  # Length of substring needed as output
        head = 0

        while current < len(s):
            # If current character is present in map in decrease counter
            # subract one entry from map and increment the 'current' pointer
            if count_map[ord(s[current])] > 0:
                counter -= 1
            count_map[ord(s[current])] -= 1
            current += 1

            while counter == 0:   # substring is valid
                # Check if current length is minimum and store the position
                if current-start < min_length:
                    min_length = current-start
                    head = start
                
                # Now move the start pointer, but do check if map entry for start pointer is zero, before adding to the counter
                if count_map[ord(s[start])] == 0:
                    counter += 1
                count_map[ord(s[start])] += 1
                start += 1

        return s[head:head+min_length] if min_length != float('inf') else ""