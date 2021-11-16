import heapq

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        hashmap = {}
        for c in s:
            if c in hashmap:
                hashmap[c] += 1
            else:
                hashmap[c] = 1
        
        minheap = []
        for i in hashmap.items():
            heapq.heappush(minheap, (i[1],i[0]))
        
        output = ''
        for i in heapq.nsmallest(len(minheap), minheap)[::-1]:
            output += i[1]*i[0]
        
        return output