class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)

        # Hashmap to store 2 str
        mapS, mapT = {}, {}

        for c in s:
            mapS[c] = 1 + mapS.get(c, 0)
        for c in t:
            mapT[c] = 1 + mapT.get(c, 0)

        # for i in range(len(mapS)):
        #     if mapS[i] != mapT[i]:
        #         return False
        return mapS == mapT