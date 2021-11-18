class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        mem = [-1 for i in range(len(s) + 1)]
        ans = self.breakit(s, wordDict, mem)
        ## print(mem)
        return ans

    def breakit(self, s, wordDict, mem):
        n = len(s)
        if mem[n] == 1 or n == 0:
            return True
        elif mem[n] == 0:
            return False

        validBreak = self.findValidBreak(s, wordDict)
        ## print(validBreak)
        for i in validBreak:
            if self.breakit(s[:i], wordDict, mem):
                mem[n] = 1
                return True
        mem[n] = 0
        return False

    def findValidBreak(self, s, wordDict):
        result = []
        for word in wordDict:
            length = len(word)
            if not len(s) - length in result and s[length * -1 :] == word:
                result.append(len(s) - length)

        ## print(result)
        return result


'''
class Solution1(object):
    ##Slow Recursive way
    Dict = []

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        self.Dict = filter(lambda x: len(x) <= len(s), wordDict)
        self.Dict = sorted(self.Dict, key=len)[::-1]
        ## print(self.Dict)
        isValid = self.findValid(s)

        return isValid
        
    def findValid(self, s):
        if len(s) == 0:
            return True

        validLength = self.findValidlength(s)
        for i in validLength:
            if self.findValid(s[i:]):
                return True
        return False

    def findValidlength(self, s):
        result = []
        for word in self.Dict:
            if s.find(word) == 0 and not len(word) in result:
                result.append(len(word))
        ## print(result)
        return result
'''
