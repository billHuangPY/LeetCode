class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left < right:
            p = left + int((right-left)/2)
            if p > 0 and nums[p] < nums[p-1]:
                return nums[p]
            elif nums[p] < nums[right]:
                right = p - 1
            else:
                left = p + 1
        return nums[left%len(nums)]