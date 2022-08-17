class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        morse_dict = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ## mp to store hash of each morse transformation
        mp = {}
        for word in words:
            ## transform the word to morse
            morse = "".join(morse_dict[ord(c)-ord('a')] for c in word)
            mp[morse] = 1
        return len(mp)