class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev_count, beams = 0, 0

        for row in bank:
            count = row.count('1')
            if count == 0: continue
            
            if prev_count != 0:
                beams += prev_count*count

            prev_count = count

        return beams