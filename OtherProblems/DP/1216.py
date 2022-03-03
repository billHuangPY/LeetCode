class Solution(object):
    def isValidPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        opt = []
        for i in range(len(s)):
            opt.append([[True for k_ in range(k+1)] for j in range(len(s))])
            
        for d in range(1, len(s)):
            for i in range(len(s)-d):
                j = i + d
                for k_ in range(k+1):
                    if s[i] == s[j]:
                        #print(i, j, 'equal')
                        opt[i][j][k_] = opt[i+1][j-1][k_]
                    elif k_ == 0:
                        #print(i, j, 'k=0')
                        opt[i][j][k_] = False
                    else:
                        opt[i][j][k_] = opt[i+1][j][k_-1] or opt[i][j-1][k_-1]
                        #print(i, j, 'not equal, k=', k_)
                    #print(i, j, k_, opt[i][j][k_])
                    if opt[i][j][k_]:
                        break
        #print(opt)
        
        return opt[0][len(s)-1][k]
        #return self.isValidPalindromeRec(s, 0, len(s)-1, k)
    
    def isValidPalindromeRec(self, s, i, j, k):
        if k < 0:
            return False
        i_, j_ = i, j
        while i_ < j_:
            if s[i_] == s[j_]:
                i_ += 1
                j_ -= 1
            else:
                return self.isValidPalindromeRec(s, i_+1, j_, k-1) or self.isValidPalindromeRec(s, i_, j_-1, k-1)
        return True
        