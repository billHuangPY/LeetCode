class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        if len(prices) <= 1:
            return 0
        dp_hadstock = -prices[0]-fee
        dp_nostock = 0

        for i in range(1,len(prices)):
            dp_hadstock = max(dp_hadstock, dp_nostock-prices[i]-fee)
            dp_nostock = max(dp_nostock, dp_hadstock+prices[i])
        
        return dp_nostock
