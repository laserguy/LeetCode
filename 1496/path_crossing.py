class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        loc_map = {}
        loc_map[(0,0)] = True

        for p in path:
            if p == 'N': y += 1
            elif p == 'S': y -= 1
            elif p == 'E': x += 1
            else: x -= 1

            if (x,y) in loc_map: return True
            else: loc_map[(x,y)] = True
        return False