class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if not nums:
            return None
        

        minNum = nums[0]
        # Brute force method, using for loop
        for num in nums:
            minNum = min(minNum, num)
        
        return minNum