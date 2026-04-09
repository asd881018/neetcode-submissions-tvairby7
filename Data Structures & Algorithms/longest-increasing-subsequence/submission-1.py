class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # [9,1,4,2,3,3,7]
        # 9
        # 1, 4, 7   -> LIS[1] = max(LIS[1], 1 + LIS[2])
        #    4, 7
        
        # 1, 2, 3, 7 -> LIS[1] = max(LIS[1], 1 + LIS[3])

        #            -> LIS[1] = max(LIS[1], 1 + LIS[2], 1 + LIS[3])                    

        #    2, 3, 7
        #       3, 7
        #          7

        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)

    
