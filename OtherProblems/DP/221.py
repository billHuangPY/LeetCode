class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        max_len = 0
        opt = []

        for i in range(len(matrix)):
            a = []
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    a.append(1)
                    max_len = 1
                else:
                    a.append(0)
            opt.append(a)
        #print(opt)
        
        if max_len == 0:
            return 0
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    opt[i][j] = min(opt[i-1][j], opt[i][j-1], opt[i-1][j-1]) + 1
                    if opt[i][j] > max_len:
                        max_len = opt[i][j]
        
        return max_len*max_len

    def maximalSquare2(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        diag = 0
        max_len = 0
        opt = []
        for i in range(len(matrix[0])):
            if matrix[0][i] == '1':
                opt.append(1)
                max_len = 1
            else:
                opt.append(0)
                
        for i in range(len(matrix)):
            if matrix[i][0] == '1':
                max_len = 1
        
        for i in range(1, len(matrix)):
            diag = int(matrix[i-1][0])
            opt[0] = int(matrix[i][0])
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == '1':
                    value = min(diag, opt[j], opt[j-1]) + 1
                    if value > max_len:
                        max_len = value
                else:
                    value = 0
                diag = opt[j]
                opt[j] = value
            #print(opt)
        
        return max_len*max_len