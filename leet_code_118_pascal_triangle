class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        dp = []
        # Base case 0 1

        for i in range(numRows):
            ls = [0]* (i+1)
            ls[0] = 1
            ls[i] = 1
            for j in range (i):
                if ls[j] == 0:
                    ls[j] = dp[i-1][j] + dp[i-1][j-1]
            dp.append(ls)
        return dp
        


