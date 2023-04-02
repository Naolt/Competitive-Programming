class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        val = bool(n&1)
        k = 1 << 1
        while n > 0:
            if n & k:
                if val:
                    return False
                val = True
            else:
                if not val:
                    return False
                val = False
            n >>= 1
        return True