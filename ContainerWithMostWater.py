class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        i = 0
        j = len(height)-1
        while(i < j):
            maxArea = max(min(height[i],height[j]) * (j-i),maxArea)
            if(height[i]> height[j]):
                j-=1
            else:
                i+=1
        return maxArea
