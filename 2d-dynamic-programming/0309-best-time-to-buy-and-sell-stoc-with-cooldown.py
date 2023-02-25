class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i, state):
            if i >= len(prices):
                return 0
            if (i, state) in dp:
                return dp[(i, state)]
            if state == "sell":
                dp[(i, state)] = max(prices[i] + dfs(i+2, "buy"), dfs(i+1, "sell"))
                return dp[(i, state)]
            if state == "buy":
                dp[(i, state)] = max(dfs(i+1, "sell") - prices[i], dfs(i+1, "buy"))
                return dp[(i, state)]
        
        return dfs(0, "buy")