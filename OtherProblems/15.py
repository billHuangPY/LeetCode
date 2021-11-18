class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        for index, i in enumerate(nums):
            if index + 2 >= len(nums):
                break
            if index >= 1 and i == nums[index - 1]:
                continue

            left, right = index + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == -i:
                    ans.append([i, nums[left], nums[right]])
                    while left < right and nums[left + 1] == nums[left]:
                        left += 1
                    left += 1
                elif nums[left] + nums[right] < -i:
                    left += 1
                else:
                    right -= 1

        return ans
