import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        bucket = [[] for i in range(len(nums) + 1)]
        for i in hashmap.items():
            bucket[i[1]].append(i[0])

        output = []
        output_len = 0
        for i in bucket[::-1]:
            for j in i:
                output.append(j)
                output_len += 1
                if output_len == k:
                    break
            if output_len == k:
                break

        return output

    def topKFrequent2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in nums:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1

        min_heap = []
        for i in hashmap.items():
            heapq.heappush(min_heap, (i[1], i[0]))

        output = []
        for i in heapq.nsmallest(len(nums), min_heap)[-k:]:
            output.append(i[1])

        return output
