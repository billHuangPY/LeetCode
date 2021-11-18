import collections


class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = sorted(collections.Counter(nums).items())

        opt, prev = [0, nums_dict[0][0] * nums_dict[0][1]], nums_dict[0][0]
        for i in nums_dict[1:]:
            if i[0] - 1 > prev:
                opt.append(opt[-1] + i[0] * i[1])
            else:
                opt.append(max(opt[-1], i[0] * i[1] + opt[-2]))
            prev = i[0]
        return opt[-1]
