class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        group = []
        curr = 1
        for i in range(1, len(s)):
            if not s[i] == s[i - 1]:
                group.append(curr)
                curr = 1
            else:
                curr += 1
        group.append(curr)

        count = 0
        for i in range(1, len(group)):
            count += min(group[i - 1], group[i])

        return count
