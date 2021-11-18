class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left, right = 0, len(letters) - 1
        while left <= right:
            p = left + int((right - left) / 2)
            if letters[p] > target:
                right = p - 1
            else:
                left = p + 1
        return letters[left % len(letters)]
