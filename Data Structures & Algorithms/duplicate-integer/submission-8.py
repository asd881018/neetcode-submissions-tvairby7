class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # Nested loop, check nums[i] == nums[j]
        # Hashmap, iterate all the element, then check if any count > 1 of each item
        # HashSet, we visit one, check hashset, if not exist, store in the hashset

        visit = set()

        for num in nums:
            if num in visit:
                return True
            visit.add(num)

        return False