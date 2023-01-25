   
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        size = len(piles)
        return sum(sorted(piles)[(size//3)::2])
        