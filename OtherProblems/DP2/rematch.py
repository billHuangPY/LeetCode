class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        dptable = {}
        return self.findMatch(s, p, dptable)
    
    def findMatch(self, s, p, dptable):
        state = s + '-' + p
        if state in dptable.keys():
            return dptable[state]

        returnValue = False
        ## if the pattern is empty, check if the input is empty
        if len(p) == 0:
            returnValue = len(s) == 0
        else:
            ## check if the first character matches the first character of pattern
            matchfirst = (not len(s) == 0 and (s[0] == p[0] or p[0] == '.'))
            ## if there is a star sign, we need to check two possibilities, (1) no such character matches the pattern, (2) match the pattern but possibly match again
            if len(p) >= 2 and p[1] == '*':
                returnValue = self.findMatch(s, p[2:], dptable) or (matchfirst and self.findMatch(s[1:], p, dptable))
            ## if there is no star sign, check if the first character matches, if matches find the subset of the problem
            else:
                returnValue = matchfirst and self.findMatch(s[1:], p[1:], dptable)
        
        dptable[state] = returnValue
        return returnValue
