class Solution:
    def isAlpha(self, c: chr) -> bool:
        ## check if char is in 0~9, A~Z, a~z
        return (ord('0') <= ord(c) <= ord('9') or 
                ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z'))
    
    def isPalindrome(self, s: str) -> bool:
        
        # Two pointer: left and right
        l = 0
        r = len(s) - 1

        while l < r:
            # Check s[l] and s[r] are alpha
            while l < r and not self.isAlpha(s[l]):
                l+=1
            while l < r and not self.isAlpha(s[r]):
                r-=1

            if s[l].lower() != s[r].lower():
                return False
            l+=1
            r-=1
        
        return True
     