import collections

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        len_rN = len(ransomNote)
        if len(magazine) < len_rN:
            return False
        
        mp = collections.Counter(magazine)
                
        for n in ransomNote:
            if mp[n] <= 0:
                return False
            mp[n] -= 1
                
        return True