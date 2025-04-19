# 1318. Minimum Flips to Make a OR b Equal to c


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        res = 0
        while c > 0 or a > 0 or b > 0:
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1
            if bit_c == 0:
                res += bit_a + bit_b
            else:
                if bit_a == 0 and bit_b == 0:
                    res += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return res
