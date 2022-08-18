def two_sum(nums, k):
    ## mp to store where the visited number locates
    mp = {}
    for idx, num in enumerate(nums):
        ## sub to find out the number needed to get the sum to target k
        sub = k - num
        ## find if sub already exists
        if sub in mp:
            return True
        ## if not existed yet, store the current index into mp
        mp[num] = idx

    return False

print(two_sum([4,7,1,-3,2], 5))
# True


'''
For Leetcode twosum, need to find the indices

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for idx, num in enumerate(nums):
            sub = target - num
            if sub in mp:
                return [idx, mp[sub]]
            mp[num] = idx
        return [-1,-1]
'''