class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = []
        for i in range(len(nums)):
            best = self.getmax(result, nums, i)
            result.append(best + 1)
        
        print(result)
        return max(result)
    
    def getmax(self, result, nums, n):
        max = 0
        for i in range(len(result)):
            if  nums[i] < nums[n]:
                value = result[i]
                if value > max:
                    max = value
        return max