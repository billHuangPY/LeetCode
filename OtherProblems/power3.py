class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        ## find out the max number that power of 3 (3**19) 
        ## smaller than limit (2**30)
        return n > 0 and 1162261467 % n == 0