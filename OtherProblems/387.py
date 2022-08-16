import collections

class Solution:
    ## fastest and least memory
    def firstUniqChar(self, s: str) -> int:
        ## create a collection counter to store frequency of each character
        counted = collections.Counter(s)
        ## iterate over the string to find the first character having frequency of 1
        for i, c in enumerate(s):
            if counted[c] == 1:
                return i
        return -1

'''
class Solution:
    ## using simple hashmap, list storing real index
    def firstUniqChar(self, s: str) -> int:
        ## mp to store the index of each characters
        mp = {}
        for i in range(len(s)):
            c = s[i]
            ## if mp already has this character, then append the index to the list
            if c in mp:
                mp[c].append(i)
            ## if mp not yet has this character as key, create the instance of current index
            else:
                mp[c] = [i]
        ## check the mp iteratively to find which character's index list has only one index
        for item in list(mp.items()):
            if len(item[1]) == 1:
                return item[1][0]
        return -1
    
class Solution:
    ## using simple hashmap, list storing only occurrence
    def firstUniqChar(self, s: str) -> int:
        ## mp to store the index of each characters
        mp = {}
        for c in s:
            ## if mp already has this character, the occurrence add 1
            if c in mp:
                mp[c] += 1
            ## if mp not yet has this character as key, create the instance of 1
            else:
                mp[c] = 1
        ## check the s iteratively to find which character's mp value = 1, means only one occurrence
        for i, c in enumerate(s):
            if mp[c] == 1:
                return i
        return -1
'''