class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans = ""
        
        ## mp to store the occurrence of each character
        mp = {}
        for c in t:
            if c in mp:
                mp[c] += 1
            else:
                mp[c] = 1
        
        ## currlen to store current length of matching characters
        ## left and write are the sliding window pointers
        currlen = 0
        left, right = 0, 0
        ## break the loop if right pointer out of bound
        while right < len(s) and right >= left:
            ## if the right pointer point to a matching character in mp
            ## the number in mp goes down
            if s[right] in mp:
                mp[s[right]] -= 1
                ## but only if the occurrence doesn't exceed the need.
                ## the currlen of matching characters increase
                if mp[s[right]] >= 0:
                    currlen += 1
            ## if th currlen equal the length of target string
            ## means current windows is a valid substring containing all
            ## required elements in t
            if currlen == len(t):
                ## if the left pointer doesn't point to a character in 
                ## mp, or the occurrence exceed the need, keep moving 
                ## left pointer until it matches and have exact the required
                ## occurrence in current window
                while not s[left] in mp or mp[s[left]] < 0:
                    ## if it is one of the duplicate character, decrease the 
                    ## occurrence in mp, which is to increase the mp value
                    if s[left] in mp:
                        mp[s[left]] += 1
                    left += 1
                ## to this point, right pointer pointing a character such that
                ## the substring contains all required elements of t, and left
                ## pointer also point to a non-duplicated character. That is,
                ## this is a current minimum window, we compare to current minimum
                ## length of the string, if it's the first one or the length is
                ## smaller than record, update the record
                if not ans or right - left + 1 < len(ans):
                    ans = s[left:right+1]
                ## current window ends reviewing, move the left pointer, uncount the 
                ## character of current left pointed one, and decrease the current matching
                ## length
                mp[s[left]] += 1
                left += 1
                currlen -= 1
                
            right += 1
            
        
        return ans
            
            
        