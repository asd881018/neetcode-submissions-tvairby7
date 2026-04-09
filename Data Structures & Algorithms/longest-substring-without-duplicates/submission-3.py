class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        if len(s) < 1:
            return 0

        maxLength = 0

        start = 0

        for end in range(len(s)):
            
            while s[end] in seen:
                seen.remove(s[start])
                start += 1
                
            seen.add(s[end])

            curLength = end - start + 1
            maxLength = max(maxLength, curLength)

        return maxLength
