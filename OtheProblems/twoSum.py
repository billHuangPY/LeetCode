class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, i in enumerate(nums):
            i_comp = target - i
            if i_comp in hashmap:
                return [index, hashmap[i_comp]]
            hashmap[i] = index
        return

class SolutionQuestion(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_num = sorted(nums)
        found = False
        half = int(target / 2)
        sorted_ans = [0, 1]
        for i in range(len(sorted_num)):
            if sorted_num[i] == half:
                sorted_ans[0] = i
                sorted_ans[1] = i + 1
                break
            elif sorted_num[i] > half:
                sorted_ans[0] = i-1
                sorted_ans[1] = i
                break
        
        while not found and sorted_ans[0] >= 0 and sorted_ans[1] < len(nums):
            #print(sorted_ans)
            if sorted_num[sorted_ans[0]] + sorted_num[sorted_ans[1]] > target:
                sorted_ans[0] -= 1
            elif sorted_num[sorted_ans[0]] + sorted_num[sorted_ans[1]] < target:
                sorted_ans[1] += 1
            else:
                found = True
                
        sorted_ans = [sorted_num[i] for i in sorted_ans]
        ans = []
        for i in range(len(nums)):
            if nums[i] in sorted_ans:
                ans.append(i)
                if len(ans) == 2:
                    break
        return ans
