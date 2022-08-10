class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        lib = {}
        for num in nums:
            if num in lib:
                del lib[num]
            else:
                lib[num] = 1
        return list(lib.keys())[0]