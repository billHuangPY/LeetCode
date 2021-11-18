class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n <= 2:
            return 1

        curr, prev1, prev2, curr_fib = 2, 0, 1, 1
        while curr < n:
            prev1, prev2, curr_fib = prev2, curr_fib, prev1 + prev2 + curr_fib
            curr += 1
        return curr_fib
