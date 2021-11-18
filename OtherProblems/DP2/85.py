class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        dp_h, dp_v = [], []
        for i in matrix:
            dp_h.append([0 for j in matrix[0]])
            dp_v.append([0 for j in matrix[0]])

        max_area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0:
                    dp_v[i][j] = int(matrix[i][j])
                elif matrix[i][j] == "1":
                    dp_v[i][j] = dp_v[i - 1][j] + 1

                if j == 0:
                    dp_h[i][j] = int(matrix[i][j])
                elif matrix[i][j] == "1":
                    dp_h[i][j] = dp_h[i][j - 1] + 1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if dp_h[i][j] == 1 or dp_v[i][j] == 1:
                    max_area = max(max_area, dp_h[i][j], dp_v[i][j])
                    continue
                if dp_h[i][j] == 0:
                    continue

                h, w = dp_v[i][j], dp_h[i][j]
                area = max(h, w)
                for k in range(w):
                    h = min(h, dp_v[i][j - k])
                    area = max(area, h * (k + 1))
                # print(i, j, area)
                max_area = max(max_area, area)

        return max_area


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        dp_v = []
        for i in matrix:
            dp_v.append([0 for j in matrix[0]])

        max_area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i == 0:
                    dp_v[i][j] = int(matrix[i][j])
                elif matrix[i][j] == "1":
                    dp_v[i][j] = dp_v[i - 1][j] + 1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                h = dp_v[i][j]
                k, area = j, h
                while k >= 0 and matrix[i][k] == "1":
                    h = min(h, dp_v[i][k])
                    area = max(area, h * (j - k + 1))
                    k -= 1
                max_area = max(area, max_area)

        return max_area
