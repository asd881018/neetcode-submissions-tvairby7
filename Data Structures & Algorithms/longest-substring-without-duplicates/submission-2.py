class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0
        
        visit = set()
        count, maxCount = 1, 1

        # "zxyzxyz"
        # "zxy"
        # " xyz"

        # need an index to store where we start the substring

        for i, c in enumerate(s):
            j = i + 1
            visit.add(c)
            # another for/while loop for iterate substring
            while j < len(s) and s[j] not in visit:
                count += 1
                maxCount = max(maxCount, count)
                visit.add(s[j])
                j += 1
            # reset
            count = 1
            visit = set()
        return maxCount

                    
            
            
        
    

