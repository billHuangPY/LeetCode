class Solution(object):
    def longestArithArrayLength(self, a, b):
        """
        :type a, b: List[int]
        :rtype: int
        """
        if a[0] > a[1]:
            a = a[::-1]

        maxdiff = self.findmaxdiff(a)
        max_len = -1
        ## Try all the possible diff
        for diff in range(1, maxdiff + 1):
            ## print("now diff", diff)
            current_len = 1

            ## test if b has elements smaller than a[0]
            current_num = a[0]
            while current_num - diff in b:
                current_len += 1
                current_num -= diff
                ## print("prev",current_num)
            ## print("prev len", current_len)
            ## test if a can be arithmetic array with the insertion of b elements
            current_num = a[0]
            found = True

            i = 0
            while i < len(a) - 1:
                next_num = current_num + diff
                ## print(i)

                if next_num == a[i + 1]:
                    ## print("inside, ona",current_num, next_num)
                    current_len += 1
                    current_num = next_num
                    ## print("curr len", current_len)
                    if i == len(a) - 2:
                        ## print("break")
                        break

                elif next_num in b:
                    ## print("inside, onb",current_num, next_num)
                    ## print(i)
                    current_len += 1
                    current_num = next_num
                    ## print("curr len", current_len)
                    i -= 1

                else:
                    found = False
                    break

                i += 1

            if not found:
                continue

            ## test if b has elements greater than a[n]
            while current_num + diff in b:
                current_len += 1
                current_num += diff
                ## print("post",current_num)
                ## print("curr len", current_len)
            print(diff, current_len)
            max_len = max(max_len, current_len)

        return max_len

    def findmaxdiff(self, a):
        maxdiff = 10 ** 6
        for i in range(len(a) - 1):
            maxdiff = min(a[i + 1] - a[i], maxdiff)
        return maxdiff


a, b = [0, 6, 12], [-6, 2, 4, 16, 8, 10, 18, 24, 26, 35]
sol = Solution()
print(sol.longestArithArrayLength(a, b))
