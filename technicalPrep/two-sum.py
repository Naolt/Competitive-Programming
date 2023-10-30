class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numDict = defaultdict(int)

        for index,num in enumerate(nums):
            if target-num in numDict:
                return [numDict[target-num],index]
            numDict[num] = index

         