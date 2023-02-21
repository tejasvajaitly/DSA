class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # O(n)/O(1) : Time/Memory
        res = nums[0]
        currMin, currMax = 1, 1
        
        for n in nums:
            tmp = currMin
            currMin = min(currMin * n, currMax * n, n)
            currMax = max(tmp * n, currMax * n, n)
            res = max(res, currMax)
        return res
