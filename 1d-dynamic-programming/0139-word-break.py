class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and w == s[i : i + len(w)]:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        
        return dp[0]

# note
# We build a boolean array where the ith element is true if the substring up to the ith character can be segmented into words from the dictionary.