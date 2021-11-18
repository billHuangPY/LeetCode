class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        result = 0
        if len(intervals) <= 1:
            return result

        sorted_intervals = sorted(intervals, key=lambda x: x[1])
        curr = sorted_intervals[0]
        for interval in sorted_intervals[1:]:
            if interval[0] < curr[1]:
                result += 1
            else:
                curr = interval

        return result
