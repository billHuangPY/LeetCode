from minheap import MinHeap

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        minheap = MinHeap()
        for i in nums:
            if minheap.get_size() < k:
                minheap.insert(i)
            else:
                if minheap.get_min() < i:
                    minheap.del_min()
                    minheap.insert(i)
        
        return minheap.get_min()

class Solution2(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        return nums[-k]
