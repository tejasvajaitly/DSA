class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dfs solution
        dp = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            if i in dp:
                return dp[i]
            maximum = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    maximum = max(maximum, 1 + dfs(j))
            dp[i] = maximum
            return maximum
        
        res = 1
        for i in range(len(nums)):
            res= max(res, dfs(i))
        
        return res

        #true dp solution

        dp = [1] * len(nums)
        res = 1
        for i in range(len(nums) - 1, -1, -1):
            maximum = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    maximum = max(maximum, 1 + dp[j])
            dp[i] = maximum
            res = max(res, maximum)
        return res