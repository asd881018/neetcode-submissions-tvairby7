class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False

        ## Hashmap to store the char
        mapS, mapT = {}, {}

        for i in range(len(s)):
            mapS[s[i]] = 1 + mapS.get(s[i], 0) 
            mapT[t[i]] = 1 + mapT.get(t[i], 0)

        ## Compare
        return mapS == mapT
        