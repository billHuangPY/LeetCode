class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return 1
        prev, preprev = 1, 1
        for i in range(2, n+1):
            prev, preprev = prev+preprev, prev
        return prev