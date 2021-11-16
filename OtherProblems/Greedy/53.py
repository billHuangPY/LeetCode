class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        prefix = [0]
        sum_ = 0
        for i in nums:
            sum_ += i
            prefix.append(sum_)
        
        print(prefix)
        min_ = prefix[0]
        max_diff = prefix[1]
        for i in prefix[1:]:
            max_diff = max(max_diff, i - min_)
            min_ = min(i, min_)
        return max_diff
        
    
    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr, max_ = nums[0], nums[0]
        for i in nums[1:]:
            curr = max(curr+i, i)
            max_ = max(max_, curr)
        return max_