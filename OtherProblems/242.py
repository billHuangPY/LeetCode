
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## if the length is different, no chance to be anagram
        if not len(s) == len(t):
            return False
        
        ## give all alphabet a counter
        mp = [0]*26
        ## iterate both string to count the counter
        for i in range(len(s)):
            ## the alphabet appears in s increase the counter
            mp[ord(s[i])-97] += 1
            ## the alphabet appears in t decrease the counter, means the character is counted
            mp[ord(t[i])-97] -= 1
        ## check there is only zero in the counter list
        for n in mp:
            if not n == 0:
                return False
        return True

'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        
        ## mp to store the number of occurence of each character in s
        mp = {}
        ## assign the map value of each character
        for s_ in s:
            if not s_ in mp:
                mp[s_] = 1
                continue
            mp[s_] += 1
        ## decrease the counter of each character has been counted in t
        for t_ in t:
            ## if the counter of that character not greater than 0, than it is not anagram
            if not t_ in mp or mp[t_] <= 0:
                return False
            mp[t_] -= 1
        return True
'''