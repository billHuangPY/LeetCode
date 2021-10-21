class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g_sorted, s_sorted = sorted(g), sorted(s)
        g_index, s_index = 0, 0
        
        while g_index < len(g) and s_index < len(s):
            if g_sorted[g_index] <= s_sorted[s_index]:
                g_index += 1
                s_index += 1
            else:
                s_index += 1
                
        return g_index