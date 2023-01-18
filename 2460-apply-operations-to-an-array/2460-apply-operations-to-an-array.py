class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        result = []
        zeroCount = 0
        size = len(nums)
        for i in range(1,size):
            if nums[i-1] == nums[i]:
                nums[i-1] *= 2
                nums[i] = 0
                
            if nums[i-1] == 0:
                zeroCount += 1
            else:
                result.append(nums[i-1])
        if nums[size-1] == 0:
            zeroCount += 1
        else:
            result.append(nums[size-1])
        
        for i in range(zeroCount):
            result.append(0)
            
        return result