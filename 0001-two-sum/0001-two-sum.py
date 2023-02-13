class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        
        for i,num in enumerate(nums):
            if num in numDict:
                return [numDict[num],i]
            numDict[target-num] = i