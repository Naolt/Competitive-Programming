"""
1 0
2 01
3 0110
4 01101001
5 0110100110010110

"""


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        size = 2**(n-1)
        mid = size // 2
        if k <= mid:
            answer = self.kthGrammar(n-1,k)
            return answer
        else:
            answer =  self.invert(self.kthGrammar(n-1,(k-1)%mid+1))
            return answer
            
    def invert(self,s):
        if s == 0:
            return 1
        else:
            return 0