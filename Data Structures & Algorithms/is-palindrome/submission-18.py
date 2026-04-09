class Solution:
    def isAlphaNum(self, c) -> bool:
        if c == ' ':
            return False
        # if not Ord(0) - Ord(9) or not Ord(A) - Ord(Z) or not Ord(a) - Ord(z)
        return ord('0') <= ord(c) <= ord('9') or ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z')


    def isPalindrome(self, s: str) -> bool:
        # use two pointer
        length = len(s)
        l, r = 0, length-1

        while (l < r):
            # skip non alpha and num, and still l < r
            # lower case
            while (l < r and not self.isAlphaNum(s[l])):
                l += 1
            while (l < r and not self.isAlphaNum(s[r])):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True