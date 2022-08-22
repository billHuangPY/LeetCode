'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        prev = -10**6
        res = []
        for i, num in enumerate(nums[:-2]):
            if num > 0:
                break
            if num == prev:
                continue
            prev = num
            self.twoSumII(nums, i, res)
        return res
            
    
    def twoSumII(self, nums, i, res):
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum == 0:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo-1]:
                    lo += 1
            elif sum > 0:
                hi -= 1
            else:
                lo += 1
'''
## My approach
## Time: O(n^2), Memory: O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = {}
        mp = {}
        visited = {}
        for idx, num in enumerate(nums):
            if num in mp:
                mp[num].append(idx)
            else:
                mp[num] = [idx]
        ## print(mp)
        
        for idx, left in enumerate(nums[:-2]):
            if left in visited:
                continue
            visited[left] = True
            target = -left
            for j in range(idx+1, len(nums)):
                sub = target - nums[j]
                if sub in mp:
                    candidate_list = [left, nums[j], sub]
                    key = ",".join([str(x) for x in sorted(candidate_list)])
                    if not key in ans:
                        for n in mp[sub]:
                            if n > j:
                                ans[key] = candidate_list
        ## print(ans)
        return [x[1] for x in ans.items()]
'''
