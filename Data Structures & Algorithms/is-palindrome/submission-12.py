class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # helper function, see if it is space, special char
        def isAlphaNumber(c) -> bool:
            return ('0' <= c <= '9') or ('a' <= c <= 'z') or ('A' <= c <= 'Z') 

        # use l, r to see if they are the same
        l, r = 0, len(s) - 1

        while l < r:
            # while l is not alpha, l < r, l++
            while not isAlphaNumber(s[l]) and l < r:
                l += 1
            # while r is not alpha, l < r, r--
            while not isAlphaNumber(s[r]) and l < r:
                r -= 1
            # Compare
            if s[l].lower() != s[r].lower():
                return False
            # l++, r--
            l += 1
            r -= 1
        return True

        

        

        