import random

class RandomizedSet:

    def __init__(self):
        self.values = []
        self.val_to_index = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.val_to_index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False

        idx = self.val_to_index[val]
        last_val = self.values[-1]

        if val != last_val:
            self.values[idx] = last_val
            self.val_to_index[last_val] = idx

        self.values.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)