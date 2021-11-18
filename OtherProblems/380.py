import random


class RandomizedSet(object):
    def __init__(self):
        self.rset = set([])

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if not val in self.rset:
            self.rset.add(val)
            return True
        else:
            return False

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.rset:
            self.rset.remove(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        :rtype: int
        """
        return random.sample(self.rset, 1)[0]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
