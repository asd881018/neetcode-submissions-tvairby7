class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums = [2,20,4,10,3,4,5]
        # sort -> [2,3,4,4,5,10,20]

        # [0, 1, 1, 2, 3, 4, 5, 6]

        if len(nums) < 1:
            return 0
        

        nums = sorted(nums)
        print(nums)
        maxLength = 1 
        curLength = 1 

        for i in range(1, len(nums)):
            prev = nums[i - 1]
            cur = nums[i]
            diff = cur - prev
            if diff == 0:
                continue
            elif diff == 1:
                curLength += 1
            else:
                curLength = 1

            maxLength = max(maxLength, curLength)

            

        return maxLength
