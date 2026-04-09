class Solution:
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
    def isPalindrome(self, s: str) -> bool:
        
        # left and right
        l = 0
        r = len(s) - 1

        while l < r:
            # check if l and r are the char or not
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while l < r and not self.alphaNum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l, r = l + 1, r - 1 

        return True