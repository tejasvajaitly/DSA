class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

#dfs method
        dp = {}

        def dfs(i, sum):
            if sum == amount:
                return 1
            if i == len(coins) or sum > amount:
                return 0
            if (i, sum) in dp:
                return dp[(i, sum)]
           
            dp[(i, sum)] = dfs(i, sum + coins[i]) + dfs(i+1, sum)
            return dp[(i, sum)]

        return dfs(0, 0)

#true dp solution

        rowPrev = [0] * (amount + 1)
        rowPrev[0] = 1
        
        for i in range(len(coins) - 1, -1, -1):
            rowCurr = [0] * (amount + 1)
            rowCurr[0] = 1
            for j in range(1, amount + 1):
                rowCurr[j] = rowPrev[j]
                if j - coins[i] >= 0:
                    rowCurr[j] += rowCurr[j - coins[i]]
            rowPrev = rowCurr

        return rowCurr[amount]