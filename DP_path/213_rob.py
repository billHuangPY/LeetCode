class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return nums[0]
        opt = [0, nums[0]]
        for i in range(1, len(nums)-1):
            opt.append(max(opt[-1], opt[-2]+nums[i]))
        max_rob = opt[-1]
        opt = [0, nums[1]]
        for i in range(2, len(nums)):
            opt.append(max(opt[-1], opt[-2]+nums[i]))
        return max(max_rob, opt[-1])