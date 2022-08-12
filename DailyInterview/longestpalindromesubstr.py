class Solution:
    def longestPalindrome(self, s: str) -> str:
        ## if the string length is smaller than 2, than itself must be a longest palindrome
        if len(s) <= 1:
            return s
        
        ## initialize the answer of string length with 0, and start at 0, end at 0
        left, right, length = 0, 0, 0
        ## iterate over all indices to expand and check if the index is the center of the longest palindrome
        for i in range(len(s)):
            ## to find the longest length (odd) of the palindrome centered at the index, i.e. index = 2 "abbba" -> len1 = 5
            lenOdd = self.getExpandedLength(s, i, i)
            ## to find the longest length (even) of the palindrome centered at the index and the next index, i.e. index = 2 "abba" -> len2 = 4
            lenEven = self.getExpandedLength(s, i, i+1)
            ## determine which gets longer length
            leni = max(lenOdd, lenEven)
            ## update the answer if length of current index longer than the answer
            if leni > length:
                ## ** Cool formula **
                left, right, length = i - (int((leni - 1)/2)), i + (int(leni/2)), leni
        ## return substring of longest palindrome
        return s[left:right+1]

    def getExpandedLength(self, s: str, left: int, right: int) -> int:
        ## Loop until current boundary can't get a palindrome or go out of boundary, 
        ## keep expanding by decreasing left and increasing right boundaries
        while left >= 0 and right < len(s) and s[left]==s[right]:
            left -= 1
            right += 1
        ## return the length of longest expanded palindrome
        return right - left - 1
