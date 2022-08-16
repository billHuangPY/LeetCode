class Solution:
    def romanToInt(self, s: str) -> int:
        ## dictionary for two character symbols
        roman_num_2 = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }
        ## dictionary for one character symbols
        roman_num = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        index, num = 0, 0
        ## iterate over the given string
        while index < len(s):
            if len(s) - index > 1:
                ## if the symbol matches in the two character dictionary, add the 
                ## number and go to next round of loop, continue looking
                ch = s[index:index+2]
                if ch in roman_num_2:
                    num += roman_num_2[ch]
                    index += 2
                    continue
            
            ## if the symbol does not match any in two character dictionary, 
            ## add the corresponding number of the symbol directly
            c = s[index]
            num += roman_num[c]
            index += 1
        return num
            
        