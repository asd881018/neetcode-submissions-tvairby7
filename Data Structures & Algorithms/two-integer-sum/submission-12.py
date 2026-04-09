class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Brute force -> Nested loop
        
        # single loop

        if (len(nums) < 2):
            return [-1, -1]

        # record the value and position we visit before
        visit = {}

        for i, num in enumerate(nums):
            # num + someValue in visit = target
            diff = target - num
            # check if diff is in visit
            if diff in visit:
                return [visit[diff], i]
            visit[num] = i
        
        return [-1, -1]