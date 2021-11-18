class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        left, right = 0, len(s) - 1
        vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        s = list(s)
        while left < right:
            while not s[left] in vowel and left < right:
                left += 1
            while not s[right] in vowel and right > left:
                right -= 1
            if right <= left:
                break

            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return "".join(s)


sol = Solution()
print(sol.reverseVowels("hello"))
