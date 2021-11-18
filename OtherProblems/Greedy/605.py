class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed.insert(0, 0)
        flowerbed.insert(len(flowerbed), 0)

        space = 0
        p = 0
        for i in flowerbed:
            # print(i)
            if i == 0:
                space += 1
            elif space > 2:
                p += int((space - 1) / 2)
                space = 0
            else:
                space = 0

        if space > 2:
            p += int((space - 1) / 2)

        # print(p)
        return p >= n
