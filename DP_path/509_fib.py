class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        if n <= 2:
            return 1

        curr, curr_fib, prev_fib = 2, 1, 1

        while curr < n:
            tmp = curr_fib + prev_fib
            prev_fib = curr_fib
            curr_fib = tmp
            curr += 1
        return curr_fib
