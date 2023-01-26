class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        cut = floor(c**0.5)
        
        left = 0
        right = cut
        
        while left <= right:
            addition = left**2 + right**2
            if addition == c:
                return True
            elif addition < c:
                left += 1
            else:
                right -= 1
        return False
            