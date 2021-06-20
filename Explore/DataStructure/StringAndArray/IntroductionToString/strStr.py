'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        '''if len(needle) == 0:
            return 0
        
        stackptr = 0
        needleptr = 0
        
        while stackptr < len(haystack):
            print('loop start ',stackptr)
            if haystack[stackptr] == needle[needleptr]:
                print('correct',haystack[stackptr])
                if needleptr == len(needle) - 1:
                    return stackptr - len(needle) + 1
                else:
                    needleptr += 1
            else:
                print('wrong',haystack[stackptr],needle[needleptr])
                needleptr = 0
            stackptr += 1
        
        return -1'''
        return haystack.find(needle)

if __name__ == "__main__":
    sol = Solution()
    teststack = 'mississippi'
    testneedle = 'issip'
    print(sol.strStr(teststack,testneedle))
        