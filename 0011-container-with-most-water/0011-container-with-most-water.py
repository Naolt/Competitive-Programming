class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        result = 0
        
        left = 0
        right = len(height)-1
        
        while left < right:
            
            area = 0
            if height[left] < height[right]:    
                area = (right - left) * height[left]
                left += 1
            else:
                area = (right - left) * height[right]
                right -= 1
            result = max(area,result)
            
        return result
            