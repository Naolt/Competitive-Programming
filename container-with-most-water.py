class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1
        result = 0

        while left < right:

            area = 0
            w = right - left
            h = min(height[right],height[left])
            area = w * h
            if height[left] < height[right]:    
                left += 1
            else:
                right -= 1

            result = max(result,area)

        return result