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


# When working with a dynamic programming approach for this problem, it's important to keep track of both the current maximum and the current minimum product, as multiplying a negative number by the current minimum can potentially result in a new maximum product.


