## Bottom-up: tabulation
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [1, 1]
        if n == 1:
            return result[1]
        else:
            for i in range(2, n + 1):
                # print(result[i-1] , '+', result[i-2])
                result.append(result[i - 1] + result[i - 2])
            return result[n]


## Top-down: memorization
class Solution2(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [1, 1]
        if n == 1:
            return result[1]
        else:
            return self.getsteps(n, result)

    def getsteps(self, n, mem):
        if len(mem) > n:
            return mem[n]

        newstep = self.getsteps(n - 1, mem) + self.getsteps(n - 2, mem)
        mem.append(newstep)
        return newstep
