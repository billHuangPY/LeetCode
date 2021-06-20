"""
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return [] 

        M, N = len(matrix[0]), len(matrix)
        found = [0]*(M*N)

        #Direction: 1, M, -1, -M
        loc, curDir = 0, 1
        newVec = []
        while 0 in found:
            print matrix[loc/M][loc%M]
            newVec.append(matrix[loc/M][loc%M])
            found[loc] = 1

            #go right
            if curDir == 1:
                if loc/M == (loc+1)/M and found[loc+1] == 0:
                    loc = loc + 1
                    print "go right"
                    continue
                else:
                    curDir = M
            #go down
            if curDir == M:
                if (loc+M)/M < N and found[loc+M] == 0:
                    loc = loc + M
                    print "go down"
                    continue
                else:
                    curDir = -1
            #go left
            if curDir == -1:
                if loc/M == (loc-1)/M and found[loc-1] == 0:
                    loc = loc - 1
                    print "go left"
                    continue
                else:
                    curDir = -M
            #go up
            if curDir == -M:
                if loc-M >= 0 and found[loc-M] == 0:
                    loc = loc - M
                    print "go up"
                    continue
                else:
                    curDir = 1
                
            loc = loc + 1

        return newVec
        