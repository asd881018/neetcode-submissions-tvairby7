class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)

        if len(s) != len(t):
            return False

        # Hashmap to store 2 str
        # mapS, mapT = {}, {}
        mapAna = {}

        # for i in range(len(s)):
        #     mapS[s[i]] = 1 + mapS.get(s[i], 0)
        #     mapT[t[i]] = 1 + mapT.get(t[i], 0)

        for i in range(len(s)):
            mapAna[s[i]] = mapAna.get(s[i], 0) + 1
            mapAna[t[i]] = mapAna.get(t[i], 0) - 1

        for key, value in mapAna.items():
            if value != 0:
                return False

        return True