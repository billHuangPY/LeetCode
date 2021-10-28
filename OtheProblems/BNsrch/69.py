class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        
        left, right = 1, x
        while left < right:
            p = left + int((right-left)/2)
            if p**2 == x or (p**2 < x and (p+1)**2 > x):
                return p
            elif p**2 < x:
                left = p + 1
            else:
                right = p - 1
        return left