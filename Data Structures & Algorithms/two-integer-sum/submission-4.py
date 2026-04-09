class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ## 1. nested for loop, check nums[i] + nums[j] == target

        ## 2. HashMap to store nums
        prevMap = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[num] = i
        