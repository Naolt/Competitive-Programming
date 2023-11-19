class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        def findMonoDec(arr,dic):
            stack = []  
            for index,num in enumerate(arr):
                if not stack or stack[-1][1] < num:
                    stack.append((index,num))
                else:
                    while stack and stack[-1][1] > num:
                        i,n = stack.pop()
                        dic[i] = index
                    stack.append((index,num))
            while stack:
                i,n = stack.pop()
                dic[i] = len(arr)
            return dic
        
        rightMonotone = findMonoDec(heights,{})
        leftMonotone = findMonoDec(heights[::-1],{})

        answer = 0
        for i in range(len(heights)):
            right = rightMonotone[i]
            left = len(heights)-leftMonotone[len(heights)-i-1]-1
            answer = max(answer,(right-left-1)*heights[i])

        return answer


        