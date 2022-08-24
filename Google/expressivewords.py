class Solution:
    def expressiveWords(self, s: str, words) -> int:
        result = 0
        smap = self.getMap(s)
        for word in words:
            if self.validWord(smap, word):
                result += 1
        return result
    
    '''
    Get the character mapping for the provided string
    Ex. heeellooo
    {"h":1, "e":3, "l":2, "o":3}
    '''
    def getMap(self, s):
        ## curr number to store current repeated number
        curr = 1
        result = []
        for i in range(len(s)):
            ## if it is the last element or next element will be different
            ## add the current value in the list
            if i == len(s) - 1 or not s[i] == s[i+1]:
                result.append((s[i], curr))
                curr = 1
            else:
                curr += 1
        return result
    
    '''
    Check if the argument word is stretchy for the string s
    '''
    def validWord(self, smap, word):
        ## curr like another method, store the number of current
        ## repeated character's occurrence. mpidx store the current index
        ## of the string mapping
        curr = 1
        mpidx = 0
        for i in range(len(word)):
            ## if the string mapping has less key length than the word
            ## return false
            if mpidx >= len(smap):
                return False
            ## if current character has end repeated or it is the last
            ## element, check if the occurrence valid, reset curr and 
            ## check next mapping index
            if i == len(word) - 1 or not word[i] == word[i+1]:
                ## if any of below condition met, return False
                ## 1. the character of mapping is different from the word
                ## 2. the occurrence from word is bigger than mapping value
                ## 3. the occurrence are not equal and the mapping value is
                ##    also smaller than 3 (if they are equal, that'd be fine)
                if not word[i] == smap[mpidx][0] or \
                    curr > smap[mpidx][1] or \
                    (not curr == smap[mpidx][1] and smap[mpidx][1] < 3):
                    return False
                ## everything passes, check next mapping index and reset curr
                curr = 1
                mpidx += 1
            else:
                curr += 1
        ## if mapping index didn't finish and the word ended counting, return
        ## False
        if mpidx < len(smap):
            return False
        return True