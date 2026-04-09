class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # [2,20,4,10,3,4,5]
        # sort
        # [2,3,4,4,5,10,20]

        # maxCount, count
        # if cur == prev, skip
        # if cur == prev + 1, count++, max(maxCount, count)
        # else: count = 1

        if not nums:
            return 0
        nums.sort()
        maxCount, count = 1, 1

        for i in range(1, len(nums)):
            cur = nums[i]
            prev = nums[i-1]
            if (cur == prev):
                continue
            elif (cur == prev + 1):
                count += 1
                maxCount = max(maxCount, count)
            else:
                count = 1
        
        return maxCount
            

        