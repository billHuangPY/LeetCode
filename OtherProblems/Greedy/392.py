class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) <= 0:
            return True

        index_s = 0
        for i in t:
            if i == s[index_s]:
                index_s += 1
                if index_s == len(s):
                    return True
        return False
