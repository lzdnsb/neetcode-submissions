class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            tmp = (n >> i) & 1 # from right to left get the bit in the position
            res += (tmp << (31-i))
        return res