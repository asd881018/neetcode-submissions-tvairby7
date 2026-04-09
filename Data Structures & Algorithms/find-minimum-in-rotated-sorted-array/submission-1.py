class Solution:
    def findMin(self, nums: List[int]) -> int:

        #  m = int((r - l) + l + 1)
        
        # [3,4,5,6,1,2]
        # l = 3, m = 6, r = 2
        # m > l > r
        # --> right partition are the smaller numbers
        # --> l = m


        # [4,5,0,1,2,3]
        # l = 4, m = 1, r = 3 
        # l > r > m
        # --> we can gurantee that interval m + 1 ~ r are not the smaller numbers
        # --> left partition are the smaler numers 
        # --> r = m

        l, r = 0, len(nums) - 1
        minN = nums[0]

        while l <= r:

            if nums[l] < nums[r]:
                minN = min(minN, nums[l])
                break

            m = (l + r) // 2
            minN = min(nums[m], minN)

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return minN

