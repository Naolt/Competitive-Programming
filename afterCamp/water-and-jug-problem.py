class Solution:
    def canMeasureWater(self, j1: int, j2: int, t: int) -> bool:
        minNum = min(j1,j2)

        if j1 + j2 < t:
            return False
        if ((j1%minNum == 0) and (j2 % minNum == 0) and (t % minNum != 0)):
            return False
        if j1 % 2 == 0 and j2 % 2 == 0 and t % 2:
            return False
        gcd_ = math.gcd(j1,j2)
        if gcd_ != math.gcd(gcd_,t):
            return False
        
        return True