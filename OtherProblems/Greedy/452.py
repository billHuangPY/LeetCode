class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) <= 1:
            return len(points)
        
        result = 1
        sorted_x = sorted(points, key=lambda x: x[1])
        curr_x = sorted_x[0][1]

        for i in sorted_x[1:]:
            if i[0] <= curr_x:
                continue
            else:
                result += 1
                curr_x = i[1]
        
        return result
