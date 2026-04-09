class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## use a map to store the num visited

        visit = {}

        for i, n in enumerate(nums):
            # nums[i] + nums[j] == target
            # diff = nums[j] = target - nums[i]
            diff = target - nums[i]

            if diff in visit:
                return [visit[diff], i]
            
            visit[nums[i]] = i
            