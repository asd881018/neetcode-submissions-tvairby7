class Solution:
    def reverseBits(self, n: int) -> int:
        
        # n && 1
        # if 0, res *= 2
        # n = n << 1

        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31 - i))

        return res