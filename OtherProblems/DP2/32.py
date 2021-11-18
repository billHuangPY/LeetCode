class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return 0

        dp = [0 for i in s]
        for i in range(1, len(s)):
            if s[i - 1] + s[i] == "()":
                dp[i] = 2 + dp[i - 2]
            elif (
                s[i - 1] + s[i] == "))"
                and i - dp[i - 1] - 1 >= 0
                and s[i - dp[i - 1] - 1] == "("
            ):
                dp[i] = 2 + dp[i - 1] + dp[i - dp[i - 1] - 2]
        # print(dp)
        return max(dp)
