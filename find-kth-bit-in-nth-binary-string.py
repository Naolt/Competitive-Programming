"""
n = 3 k = 1
k < 2**3-1 = 7//2 = 3
n = 2 k = 1
k < 2**2-1 = 3//2 = 1
n = 1 k = 1  

"""


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"

        size = (2**n)-1
        mid = math.ceil(size/2)
        print(n,k,size)
        if k < mid:
            return self.findKthBit(n-1,k)
        elif k == mid:
            return "1"
        else:
            return self.invert(self.findKthBit(n-1,size-k+1))

    def invert(self,s):
        if s == "0":
            return "1"
        else: 
            return "0"



    # def getBinary(self,n):
    #     if n == 1:
    #         return "0"
    #     behind = self.getBinary(n-1)
    #     return behind + "1" +  self.invert(behind)[::-1]

    # def invert(self,s):
    #     reverted = ''
    #     for char in s:
    #         if char == '1':
    #             reverted += '0'
    #         else:
    #             reverted += '1'
    #     return reverted