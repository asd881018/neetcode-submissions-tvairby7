class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        ## 2 HashMap, store s and t, then compare if 2 Maps are same or not

        ## 1 HashMap, store (char, int) in s, delete (char, int) in t
        ## Check if empty map 

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        return countS == countT
        
        