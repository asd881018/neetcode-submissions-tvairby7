class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # the list is sorted
        # int

        # return index if found, otherwise return -1

        # brute force -> O(N)

        # nums = [-1,0,2,4,6,8], target = 4
        # l = -1, m = 2 r = 8
        # define where the m is

        # if the target is between l <-> m or m <-> r

        # if target in l <-> m, m > tagert, m -> new r

        # else, m -> new l

        l, r = 0, len(nums) - 1

        while l <= r:
            # m = (l + r) // 2 
            # m can be buffer overflow
            # distance to m = (r - l) // 2
            m = l + ((r - l) // 2)

            if target < nums[m]:
                r = m - 1
                
            
            elif target > nums[m]:
                l = m + 1
                

            else:
                return m

        return -1