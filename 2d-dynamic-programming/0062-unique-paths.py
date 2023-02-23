class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        #dfs recursion with memoization
        dp = {}
        def dfs(i, j):
            if i == m or j == n:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if (i, j) in dp:
                return dp[(i, j)]
            totalWays = dfs(i + 1, j) + dfs(i, j + 1)
            dp[(i, j)] = totalWays
            return totalWays
        return dfs(0, 0)


        #true dp solution
        row = [1] * n
        for i in range(m - 2, -1, -1):
            newRow = [1] * n
            for j in range(n - 2, -1 , -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        return row[0]