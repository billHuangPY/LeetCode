import collections

class Solution:
    def minSetSize(self, arr) -> int:
        ## get the occurrence of each character
        mp = collections.Counter(arr)
        ## sort the occurrence and sort by the most frequent element
        ## (alt) mp = [count for _, count in mp.most_common()]
        mp = sorted(list(mp.items()), key=lambda item: item[1], reverse=True)
        target = len(arr)/2
        ## curr stores the current added number, curr_idx stores the number of different elements added on number
        curr, curr_idx = 0, 0
        for num in mp:
            curr += num[1]
            curr_idx += 1
            ## if current number greater than or equal to the half of the length, return the number of different elements
            if curr >= target:
                return curr_idx