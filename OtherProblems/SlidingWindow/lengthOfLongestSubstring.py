class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == None or len(s) == 0:
            return 0

        l = 0
        max_len = 1
        curr_substring = []

        for r in range(len(s)):
            c = s[r]
            while c in curr_substring:
                curr_substring.pop(0)
                l += 1
            curr_substring.append(c)
            max_len = max(max_len, len(curr_substring))
            
        return max_len