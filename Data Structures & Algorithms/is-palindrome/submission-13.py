class Solution:

    def isAlphaNum(c):
        # 0 - 9, a - z, A - Z
        return ord('0') < ord(c) < ord('9') or ord('A') < ord(c) < ord('Z') or ord('a') < ord(c) < ord('z')

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        def isAlphaNum(c):
        # 0 - 9, a - z, A - Z
            return c.isalnum()

        while l < r:
            # char can only be eng char, number
            # if not eng, num, move to next char
            while l < r and not isAlphaNum(s[l]):
                l += 1
            while l < r and not isAlphaNum(s[r]):
                r -= 1

            # Compare
            if s[l].lower() != s[r].lower():
                return False

            # Move to next char
            l += 1
            r -= 1

        return True
             
        