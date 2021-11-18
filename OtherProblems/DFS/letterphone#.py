class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        if digits != None and len(digits) > 0:
            map = [
                "",
                "",
                "abc",
                "def",
                "ghi",
                "jkl",
                "mno",
                "pqrs",
                "tuv",
                "wxyz",
            ]
            self.dfs(digits, 0, result, "", map)
        return result

    def dfs(self, digits, index, result, combination, map):
        if index == len(digits):
            result.append(combination)
            return

        for i in map[int(digits[index])]:
            self.dfs(digits, index + 1, result, combination + i, map)
