class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        index_1, index_2, index_sorted = m-1, n-1, m+n-1
        while index_2 >= 0 and index_sorted >= 0:
            if index_1 < 0 or nums2[index_2] >= nums1[index_1]:
                nums1[index_sorted] = nums2[index_2]
                index_2 -= 1
            else:
                nums1[index_sorted] = nums1[index_1]
                index_1 -= 1
            index_sorted -= 1
            
            