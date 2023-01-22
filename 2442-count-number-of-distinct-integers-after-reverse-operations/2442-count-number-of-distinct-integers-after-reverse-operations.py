class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        numDict = {}
        
        for num in nums:
            numDict[num] = 1
            numDict[int(str(num)[::-1])] = 1
        print(numDict)
        return len(numDict)