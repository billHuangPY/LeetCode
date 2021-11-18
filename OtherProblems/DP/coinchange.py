class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        result = [0]
        current_coins = []
        for i in range(1, amount + 1):
            ## to see if amount is one of the coins
            if i in coins:
                current_coins.append(i)
                result.append(1)
            else:
                ## walkthrough all the possible currency and get the recurrence value
                possible_list = [result[i - j] for j in current_coins]

                ## to get the minimum of valid answer (max of amount is 10**4, so I use 10**5 as maximum)
                set = 10 ** 5
                for k in possible_list:
                    if k != -1 and k < set:
                        set = k

                ## if there is no valid answer then return -1
                if set == 10 ** 5:
                    result.append(-1)
                else:
                    result.append(set + 1)

        return result[amount]
