class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix) - 1
        for i in range(len(matrix)):
            if matrix[i][0] > target:
                if not i == 0:
                    row = i-1
                    break
                else:
                    return False
        
        left, right = 0, len(matrix[row])-1
        while left < right:
            p = left + int((right-left)/2)
            if matrix[row][p] == target:
                return True
            elif matrix[row][p] > target:
                right = p - 1
            else:
                left = p + 1
        return matrix[row][left] == target