class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)
        while left <= right:
            p = left + int((right-left)/2)
            if p % 2 == 1:
                p -= 1
            if p+1 < len(nums) and nums[p] == nums[p+1]:
                left = p + 2
            else:
                right = p - 1
        return nums[left]