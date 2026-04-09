class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ## 1. nested for loop, check nums[i] + nums[j] == target

        size  = len(nums)

        for i in range(size):
            for j in range (i+1, size):
                if nums[i] + nums[j] == target:
                    return [i, j]
        retunr [0,0]