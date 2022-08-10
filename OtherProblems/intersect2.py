class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        method 1: sort and match
        num1_sorted = sorted(nums1)
        num2_sorted = sorted(nums2)
        intersec = []
        
        l, r = len(num1_sorted)-1, len(num2_sorted)-1
        while l >= 0 and r >= 0:
            if num1_sorted[l] > num2_sorted[r]:
                l -= 1
            elif num1_sorted[l] < num2_sorted[r]:
                r -= 1
            else:
                intersec.append(num1_sorted[l])
                l -= 1
                r -= 1
        return intersec
        '''
        ### method 2: build dict and lookup/check
        lib = {}
        for num in nums2:
            if num in lib:
                lib[num] += 1
            else:
                lib[num] = 1
        
        intersec = []
        for num in nums1:
            if num in lib and lib[num] > 0:
                intersec.append(num)
                lib[num] -= 1
        
        return intersec