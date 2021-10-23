class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        modified = False
        
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                
                if modified:
                    return False
                
                modified = True
                if i < 2 or nums[i-1] > nums[i] and nums[i] >= nums[i-2]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
        return True
        
        
            