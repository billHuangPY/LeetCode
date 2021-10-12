class Solution(object):
    def liftingweight(self, weights, maxCapacity):
        dp = [[] for i in range(len(weights) + 1)]
        for i in range(len(dp)):
            dp[i] = [0 for j in range(maxCapacity + 1)]
        
        weights.sort()

        for N in range(1, len(weights) + 1):
            for maxC in range(1, maxCapacity+1):
                if weights[N-1] > maxC:
                    dp[N][maxC] = dp[N-1][maxC]
                else:
                    dp[N][maxC] = max(dp[N-1][maxC-weights[N-1]] + weights[N-1], dp[N-1][maxC])
        
        return dp[len(weights)][maxCapacity]

sol = Solution()
print(sol.liftingweight([4,1,3,5,6,9], 26))