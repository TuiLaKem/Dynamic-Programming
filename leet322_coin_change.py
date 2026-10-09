import math
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [math.inf]*(amount+1)
        dp[0] = 0
        if amount == 0:
            return 0
        if len(coins) == 1 and coins[0] > amount:
            return -1
        for c in coins:
            for i in range(c,len(dp)):
                dp[i] = min(dp[i], dp[i-c] + 1)

        if dp[len(dp)-1] == math.inf:
            return -1
        else:
            return dp[len(dp)-1]

        

        
