class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        cost.append(0)
        opt = [cost[0], cost[1]]
        
        for i in range(2, len(cost)):
            opt.append(min(opt[i-1], opt[i-2]) + cost[i])
        return opt[-1]