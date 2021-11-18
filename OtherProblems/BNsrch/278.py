# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        while left <= right:
            p = left + int((right - left) / 2)
            if isBadVersion(p):
                right = p - 1
            else:
                left = p + 1
        return left
