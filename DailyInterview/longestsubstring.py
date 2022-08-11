class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        ## the map to store the next index of the duplicate character 
        next_index_map = {}
        
        left = 0
        ## slide the right pointer to iterate the string
        for right in range(len(s)):
            if s[right] in next_index_map:
                ## make sure no duplicate of character other than current one
                ## even if the character is in the map, but can be ignored cuz this line checking the index in the 
                ## map is not in current substring
                left = max(next_index_map[s[right]], left)
            ## get the max length
            result = max(result, right - left + 1)
            ## count the current character in map
            next_index_map[s[right]] = right + 1
            print(next_index_map)
        return result

print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10