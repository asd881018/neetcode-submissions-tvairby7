class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # 1. split the string to chars
        #    sort the chars
        #    for loop to check s[i] == t[i]
        return sorted(s) == sorted(t)

        # 2. Hashmap to record the count of the chars in the string
        #    return mapS == mapT
        

        # 3. HashMap
        #    char in string s, we ++ the counter of that char
        #    char in string t, we -- the counter of that char
        #    check the hashmap all store 0 for all chars