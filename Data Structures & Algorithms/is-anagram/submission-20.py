class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # 1. split the string to chars
        #    sort the chars
        #    for loop to check s[i] == t[i]

        # 2. Hashmap to record the count of the chars in the string
        #    return mapS == mapT

        mapS, mapT = {}, {}

        for c in s:

            # if 0, then 1
            # if nto 0, ++
            if c not in mapS:
                mapS[c] = 1
            mapS[c] += 1
        
        for c in t:

            # if 0, then 1
            # if nto 0, ++
            if c not in mapT:
                mapT[c] = 1
            mapT[c] += 1

        return mapS == mapT
        

        

        # 3. HashMap
        #    char in string s, we ++ the counter of that char
        #    char in string t, we -- the counter of that char
        #    check the hashmap all store 0 for all chars