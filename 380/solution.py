import random

class RandomizedSet:

    def __init__(self):
        self.hash_map = {}

    def insert(self, val: int) -> bool:
        if val in self.hash_map: return False
        self.hash_map[val] = True
        return True

    def remove(self, val: int) -> bool:
        if val not in self.hash_map: return False
        self.hash_map.pop(val)
        return True

    def getRandom(self) -> int:
        l = list(self.hash_map.keys())
        return random.choice(l)