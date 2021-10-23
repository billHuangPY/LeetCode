class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums)-1
        while left < right:
            pivot = int((left + right) / 2)
            if nums[pivot] < nums[pivot-1]:
                return nums[pivot]
            elif nums[pivot] < nums[right]:
                right = pivot
            elif nums[pivot] > nums[right]:
                left = pivot+1
            else:
                right -= 1
        return nums[left]