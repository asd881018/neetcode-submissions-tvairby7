class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = float('-inf')
        for i in range(len(nums)):
            cur = 1
            for j in range(i, len(nums)):
                cur *= nums[j]
                res = max(cur, res)
            cur = 1
        return res 

            
        