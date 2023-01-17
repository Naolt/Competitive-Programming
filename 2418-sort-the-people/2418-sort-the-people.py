class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        size = len(heights)
        
        for i in range(0,size):
            for j in range(i+1,size):
                if heights[i] < heights[j]:
                    heights[i], heights[j] = heights[j],heights[i]
                    names[i], names[j] = names[j],names[i]
        return names