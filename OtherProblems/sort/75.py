class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        start = 0
        index = 0
        end = len(nums) - 1

        while start < end and index <= end:
            if nums[index] == 0:
                nums[index] = nums[start]
                nums[start] = 0
                start += 1
                index += 1
            elif nums[index] == 2:
                nums[index] = nums[end]
                nums[end] = 2
                end -= 1
            else:
                index += 1

        return
