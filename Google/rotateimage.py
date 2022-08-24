class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(int(n/2)):
            for j in range(n-2*i-1):
                matrix[i+j][n-1-i], matrix[n-1-i][n-1-i-j], matrix[n-1-i-j][i], matrix[i][i+j] = \
                    matrix[i][i+j],\
                    matrix[i+j][n-1-i],\
                    matrix[n-1-i][n-1-i-j],\
                    matrix[n-1-i-j][i]
                