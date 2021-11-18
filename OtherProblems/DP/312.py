class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        nums.append(1)

        OPT = [[] for l in range(n + 1)]
        for l in range(n + 1):
            OPT[l] = [0 for r in range(n + 1)]

        for d in range(n):
            for l in range(n - d):
                r = l + d
                currOPT = 0
                for k in range(l, r + 1):
                    # print(l, r, k)
                    OPT_k = (
                        OPT[l][k - 1]
                        + OPT[k + 1][r]
                        + nums[l - 1] * nums[k] * nums[r + 1]
                    )
                    currOPT = max(currOPT, OPT_k)
                OPT[l][r] = currOPT

        return OPT[0][n - 1]
