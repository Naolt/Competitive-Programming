class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        numDict = collections.defaultdict(int)
        maxElem = max(nums)
        maxIndex = nums.index(maxElem)
        size = len(nums)
        newSize = size-maxIndex-1
        print(maxIndex)

        newArr = nums[maxIndex+1:]+nums[:maxIndex+1]
        stack = []
        for index,num in enumerate(newArr):
            if not stack or newArr[stack[-1]] > num:
                stack.append(index)
            else:
                if stack:
                    while stack and newArr[stack[-1]] < num:
                        numDict[stack.pop()] = index
                    stack.append(index)
        result = [-1]*size
        for i in range(size):
            if i < newSize:
                if i in numDict:
                    result[maxIndex+1+i] = newArr[numDict[i]]
            else:
                if i in numDict:
                    result[i-newSize] = newArr[numDict[i]]
    
        return result