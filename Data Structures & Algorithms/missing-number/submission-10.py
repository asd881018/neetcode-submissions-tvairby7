class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        res = len(nums)

        for i in range(len(nums)):
            res += i

        print(res)
        print(sum(nums))

        return res - sum(nums)