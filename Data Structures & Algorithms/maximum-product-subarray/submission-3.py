class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # [1, -2, 3, -4]
        
        # n = 1, min = 1, max = 1
        # n = -2, min = -2, max = 1
        # n = 3, min = -6, max = 3
        # n = -4, min = -12, max = 24

        res = max(nums)

        curMax, curMin = 1, 1

        for n in nums:
            temp = curMax

            curMax = max(curMax * n, curMin * n, n)
            curMin = min(temp * n, curMin * n, n)

            res = max(res, curMax)

        return res