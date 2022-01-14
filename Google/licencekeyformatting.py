class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.replace('-','').upper()[::-1]
        s = [s[n:n+k] for n in range(0, len(s), k)]
        
        return '-'.join(s)[::-1]