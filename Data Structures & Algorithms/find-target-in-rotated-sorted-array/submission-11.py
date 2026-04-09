class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # [3,4,5,6,0,1,2]
        # Binary search -> l, m, r as pointers

        # left sorted nums[l] < nums[m]

            # if target > nums[m]: search right (l = m + 1) OR
            # if target < nums[l] : search right
            # if target > nums[l] : search left (r = m - 1)
            
        # right sorted nums[r] > nums[m]

            # if target < nums[m]: search left
            # if target > nums[m]: 
                # if target < nums[r]: search right
                # if target > nums[r]: search left

        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m

            # left sorted
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            
            # right sorted
            else:
                if target < nums[m] or (target > nums[r]):
                    r = m - 1
                else:
                    l = m + 1
        
        return -1
                