
[1,2,3,4,5,6,7,8,9]
   
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort()
        size = len(piles)
        
        if size == 3:
            return piles[1]
        
        result = 0
        for i in range(size-1,size//3,-2):
            result += piles[i-1]
        return result