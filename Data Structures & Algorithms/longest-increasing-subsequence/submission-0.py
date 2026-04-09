class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # nums = [9,1,4,2,3,3,7]
        # brute force
        # 9
        # 1, 4, 7
        # 1, 2, 3, 7 dp[1] = max(1, 1 + dp[3], 1 + dp[2])
        #    4, 7    dp[2] = 1 + dp[6]
        #    2, 3, 7 dp[3] = 1 + dp[5]
        #       3, 7 dp[5] = 1 + dp[6]
        #          7 dp[6] = 1 (6 is the index)

        # find the value (valide neigbor) is bigger than currenct value

        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)