class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        valueDict = collections.defaultdict(lambda : -1)
        result = []
        for num in nums2:
            while stack and stack[-1] < num:
                valueDict[stack.pop()] = num
            stack.append(num)
        
        for num in nums1:
            result.append(valueDict[num])
            
        return result
        