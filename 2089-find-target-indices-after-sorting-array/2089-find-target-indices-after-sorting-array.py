class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        result = []
        size = len(nums)
        found = -1
        for i in range(1,size):
            
            smallestIndex = i
            for j in range(i,size):
                if nums[j] < nums[smallestIndex]:
                    smallestIndex = j
            
            
            if nums[smallestIndex] <= nums[i-1]:
                nums[smallestIndex],nums[i-1] = nums[i-1],nums[smallestIndex]

        for i in range(size):
            if nums[i] == target:
                result.append(i)
        
        
        return result