class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        ## Hashmap. occur in s, ++; occur in t --
        map = {}

        for char in s:
            map[char] = 1 + map.get(char, 0)
        for char in t:
            map[char] = -1 + map.get(char, 0)
        
        for char in map.values():
            if char != 0:
                return False

        return True