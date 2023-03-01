class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        return self.getBinary(n)[k-1]


    def getBinary(self,n):
        if n == 1:
            return "0"
        behind = self.getBinary(n-1)
        return behind + "1" +  self.invert(behind)[::-1]

    def invert(self,s):
        reverted = ''
        for char in s:
            if char == '1':
                reverted += '0'
            else:
                reverted += '1'
        return reverted