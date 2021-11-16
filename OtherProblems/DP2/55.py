class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        
        dp = [False for i in nums]
        dp[0] = True
        
        for i in range(len(nums)):
            if dp[i] and nums[i] > 0:
                for d in range(nums[i], 0, -1):
                    if i+d >= len(nums)-1:
                        return True
                    elif dp[i+d]:
                        break
                    dp[i+d] = True
        return False

class Solution2(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1:
            return True
        
        prev = nums[0]
        for i in range(1, len(nums)):
            if i <= prev:
                prev = max(prev, nums[i]+i)
            if prev >= len(nums)-1:
                return True
            
        return False
                