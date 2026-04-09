class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 1. nested for loop, if nums[i] == nums[j] return True
        # O(n^2)

        # 2. put the num visited into map/set, check if the new num is in the map/set or not
        # O(n)

        visit = set()

        for n in nums:
            if n in visit:
                return True
            visit.add(n)

        return False