class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # brute force:
        # res = [0] * len(nums)
        # for i in len(nums):
            # # for j in len(nums):
            # if i == j: continue
            # res = nums[i] * nums[j]
        # return res
        # O(n^2)

        # to imrpvoe to O(n)
        # can only iterate array once
        # we need some space to record

        # res = [1, 1, 1, 1] 
        # 1 -> [1, 1, 1, 1]
        # 2 -> [2, 1, 2, 2]
        # 4 -> [8, 4, 2, 8]
        # 6 -> [48, 24, 12, 8]

        total = 1

        zeros = nums.count(0)

        for n in nums:
            if n != 0:
                total *= n

        res = [0] * len(nums)

        if zeros > 1:
            return res

        for i, n in enumerate(nums):
            if zeros == 1:
                if n == 0:
                    res[i] = total
                else:
                    res[i] = 0
            else: 
                res[i] =  total // n

        return res