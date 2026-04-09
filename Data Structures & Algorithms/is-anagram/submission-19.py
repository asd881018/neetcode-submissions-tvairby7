class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        # 1. s.sort() == t.sort()
        # return sorted(s) == sorted(t)

        # 2. put s and t into map
        # compare the map for s and t

        # sMap, tMap = {}, {}

        # for i in range(len(s)):
        #     sMap[s[i]] = 1 + sMap.get(s[i], 0)
        #     tMap[t[i]] = 1 + tMap.get(t[i], 0)
        
        # return sMap == tMap

        # 3. array[26]

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True
