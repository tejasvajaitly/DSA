class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

# solution with memoization        
        dp = {}
        def dfs(p1, p2, p3):
            if p1 == len(s1) and p2 == len(s2) and p3 == len(s3):
                return True
            if p3 == len(s3) and (p1 < len(s1) or p2 < len(s2)):
                return False
            if (p1, p2, p3) in dp:
                return dp[(p1, p2, p3)]
            a = b = False
            if p1 < len(s1) and s1[p1] == s3[p3]:
                a = a or dfs(p1+1, p2, p3+1)
            if p2 < len(s2) and s2[p2] == s3[p3]:
                b = b or dfs(p1, p2+1, p3+1)
            dp[(p1, p2, p3)] = a or b
            return dp[(p1, p2, p3)]
        
        return dfs(0, 0, 0)


# true dp solution
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [([False] * (len(s2) + 1) ) for i in range(len(s1) + 1)]
        dp[len(s1)][len(s2)] = True

        for i in range(len(s1), -1, -1):
            for j in range(len(s2), -1, -1):
                if i < len(s1) and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                if j < len(s2) and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
        
        return dp[0][0]