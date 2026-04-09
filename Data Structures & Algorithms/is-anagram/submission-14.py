class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False

        ## Hashmap to store the char
        mapS, mapT = {}, {}

        for c in s:
            mapS[c] = 1 + mapS.get(c, 0)
        for c in t:
            mapT[c] = 1 + mapT.get(c, 0)
        ## Compare
        return mapS == mapT
        