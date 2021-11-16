class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(nums)-1
        while left <= right:
            p = left + int((right-left)/2)
            if nums[p] >= target:
                right = p - 1
            else:
                left = p + 1
                
        l_target = left if left < len(nums) and nums[left] == target else -1
        if l_target == -1:
            return [-1, -1]
        
        left, right = l_target, len(nums)-1
        while left <= right:
            p = left + int((right-left)/2)
            if nums[p] == target:
                left = p + 1
            else:
                right = p - 1
        return [l_target, left-1]