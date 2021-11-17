class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        opt = [1, 1]
        if n <= 1:
            return 1
        for i in range(2, n+1):
            opt.append(opt[i-1]+opt[i-2])
        return opt[-1]
            