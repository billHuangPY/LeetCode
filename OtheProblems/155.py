class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_ = None
        return None

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.insert(0, val)
        if len(self.stack) == 1 or val < self.min_:
            self.min_ = val
        return val
        

    def pop(self):
        """
        :rtype: None
        """
        pop = self.stack.pop(0)
        self.min_ = min(self.stack) if len(self.stack) > 0 else None
        return pop
        

    def top(self):
        """
        :rtype: int
        """
        top = self.stack[0] if len(self.stack) > 0 else 'null'
        return top
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()