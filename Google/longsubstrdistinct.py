class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) <= 2:
            return len(s)
        ## mp to store the last index of specific character
        mp = {}
        ans = 2
        left, right = 0, 0
        
        while right < len(s):
            mp[s[right]] = right
            right += 1
            ## if current substring have more than two distinct characters,
            ## remove the character with the smallest index in mp,
            ## and move the left pointer to the next one of that index
            if len(mp) > 2:
                idx = min(mp.values())
                del mp[s[idx]]
                left = idx + 1
            ans = max(ans, right - left)
        return ans