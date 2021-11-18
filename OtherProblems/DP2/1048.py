class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        def isPred(prev, post):
            p1, p2 = 0, 0
            while p2 < len(post) and p1 < len(prev):
                if not p1 == p2 and not prev[p1] == post[p2]:
                    return False
                elif not prev[p1] == post[p2]:
                    p2 += 1
                else:
                    p1 += 1
                    p2 += 1
            return True

        words.sort(key=lambda x: len(x))
        words_len = []
        for i in words:
            words_len.append(len(i))

        dp = []
        def_len, max_chain = len(words[0]), 1
        for i in range(len(words)):
            if words_len[i] == def_len:
                dp.append(1)
            else:
                chain = 1
                for j in range(i - 1, -1, -1):
                    if words_len[j] < words_len[i] - 1:
                        break
                    elif words_len[j] == words_len[i]:
                        continue

                    if isPred(words[j], words[i]):
                        chain = max(chain, dp[j] + 1)
                dp.append(chain)
                max_chain = max(chain, max_chain)

        return max_chain
