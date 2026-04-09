class Solution:
    def rob(self, nums: List[int]) -> int:

        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
        

        # if rob1, rob(0) + rob(2:n-1), can't rob(n) cuz 1 and n are adj

        # if not rob1, rob(1:n)

        # calulate rob(0) + rob(1:n) + rob(n)

        # nums = [2,9,8,3,6]
        # [2] -> 2
        # [2,9] -> 9
        # [2,9,8] -> 9
        # [2,9,8,3] -> 12
        # [2,9,8,3,6] -> 

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2

        
