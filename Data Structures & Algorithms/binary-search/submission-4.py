class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        sorted(nums)

        while l <= r:
            ## Find the mddile num
            m = ((r - l)//2) + l
            ## Compare mid num with target
            ## if nums[m] > target, r = m
            if nums[m] > target:
                r = m - 1
                continue
            ## if m < target, l = m
            elif nums[m] < target:
                l = m + 1
                continue
            else:
                return m

        return -1
            

        