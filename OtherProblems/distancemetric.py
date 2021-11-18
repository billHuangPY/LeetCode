class Solution(object):
    def distanceMetric(self, arr):
        arr_map = {}
        for i in range(len(arr)):
            if not arr[i] in arr_map:
                arr_map[arr[i]] = [i]
            else:
                arr_map[arr[i]].append(i)

        output = []
        for i, i_value in enumerate(arr):
            pos = arr_map[i_value]
            distance = 0
            for j in pos:
                distance += abs(i - j)
            output.append(distance)

        return output

    def distanceMetrictwoway(self, arr):
        arr_dist = [0 for i in arr]
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] == arr[j]:
                    dist = abs(i - j)
                    arr_dist[i] += dist
                    arr_dist[j] += dist

        return arr_dist


sol = Solution()
print(sol.distanceMetrictwoway([1, 2, 1, 1, 2, 3]))
