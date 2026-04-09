class Solution:

    def encode(self, strs: List[str]) -> str:

        # "4#neet4#code4#love3#you"
        # when encoding, insert the length of the str & #

        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        print(res)
        return res
        
    def decode(self, s: str) -> List[str]:
        # "4#neet4#code4#love3#you"
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            # append the actual string into res
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length

        return res
