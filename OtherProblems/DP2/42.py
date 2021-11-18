class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_left, max_right = [height[0]], [height[-1]]
        # from left
        for i in range(1, len(height)):
            max_left.append(max(max_left[i - 1], height[i]))
        for i in range(len(height) - 2, -1, -1):
            max_right.insert(0, max(max_right[0], height[i]))
        # print(max_left)
        # print(max_right)
        # print(height)

        ans = 0
        for i in range(len(height)):
            ans += min(max_left[i], max_right[i]) - height[i]
        return ans
