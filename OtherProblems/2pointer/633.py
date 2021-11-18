from math import sqrt


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left, right = 0, int(sqrt(c))
        while left <= right:
            attempt = left ** 2 + right ** 2
            if attempt == c:
                return True
            elif attempt < c:
                left += 1
            else:
                right -= 1
        return False

    def judgeSquareSum2(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for i in range(int(sqrt(c)) + 1):
            b = sqrt(c - i ** 2)
            if b == int(b):
                return True
        return False
