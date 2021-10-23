class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        s_dict = {}
        for i in range(len(s)):
            if s[i] in s_dict:
                s_dict[s[i]].append(i)
            else:
                s_dict[s[i]] = [i]
        
        s_dict = sorted(s_dict.values(), key=lambda x: x[0])
        
        result = []
        while s_dict:
            left, right = s_dict[0][0], s_dict[0][-1]
            nums = len(s_dict[0])
            for i in range(1,len(s_dict)+1):
                if i == len(s_dict) or (s_dict[i][0] > right and nums == right - left + 1):
                    for j in range(i):
                        s_dict.pop(0)
                    break
                else:
                    left = min(s_dict[i][0], left)
                    right = max(s_dict[i][-1], right)
                    nums += len(s_dict[i])
            result.append(nums)
        return result