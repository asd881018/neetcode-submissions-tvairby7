class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        ## only traverse the alpha char and numbers
        ## skip if they are not alpha char and numbers, including space
        ## when they are alpha char and numbers, use lower case to compare

        ## Use two indexs to compare the from left and right

        l, r = 0, len(s) - 1

        while (l < r):
            while (not s[l].isalnum() and l < r):
                l += 1
            while (not s[r].isalnum() and l < r):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
        
        return True
            

