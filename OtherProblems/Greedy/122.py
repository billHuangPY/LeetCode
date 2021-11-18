class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        max_price = prices[0]
        min_price = prices[0]

        for price in prices[1:]:
            if price < max_price:
                profit += max_price - min_price
                min_price = price
                max_price = price
            else:
                max_price = price
        profit += max_price - min_price
        return profit
