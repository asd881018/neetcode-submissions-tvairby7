class Solution:

    def encode(self, strs: List[str]) -> str:
        # ["Hello","World"] -> "HelloWorld"
        # insert the separator, like a special char
        # "Hello$World"
        # ["Hello$World", "World"] -> "Hello$World$World" -> ["Hello", "World", "World"]
        # insert the len of the string
        # "11$Hello$World5$World" -> ["Hello$World", "World"]
        res = ""
        for s in strs:
            length = len(s)
            res += str(length)+"#"+s

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        # "11$Hello$World5$World" -> ["Hello$World", "World"]
        i = 0
        # length + $ + actual string
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res



