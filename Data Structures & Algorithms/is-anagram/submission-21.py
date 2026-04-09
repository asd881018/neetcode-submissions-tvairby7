class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # 1. split the string to chars
        #    sort the chars
        #    for loop to check s[i] == t[i]

        # 2. Hashmap to record the count of the chars in the string
        #    return mapS == mapT

        if len(s) != len(t):
            return False

        mapS, mapT = {}, {}

        for c in s:
            mapS[c] = 1 + mapS.get(c, 0)
        
        for c in t:
            mapT[c] = 1 + mapT.get(c, 0)

        for i in range(len(s)):
            mapS[s[i]] = 1 + mapS.get(s[i], 0)
            mapT[t[i]] = 1 + mapT.get(t[i], 0)

        return mapS == mapT
        

        

        # 3. HashMap
        #    char in string s, we ++ the counter of that char
        #    char in string t, we -- the counter of that char
        #    check the hashmap all store 0 for all chars