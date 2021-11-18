class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True
        return self.validPalindromeRec(list(s), False)

    def validPalindromeRec(self, s, hasdel):
        """
        :type s: str
        :type del: bool
        :rtype: bool
        """
        if len(s) <= 1:
            return True

        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif hasdel:
                return False
            else:
                return self.validPalindromeRec(
                    s[left:right], True
                ) or self.validPalindromeRec(s[left + 1 : right + 1], True)
        return True
