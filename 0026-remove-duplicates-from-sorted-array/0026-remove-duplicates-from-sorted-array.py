class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0
        size = len(nums)
        duplicate = 0
        if size == 1:
            return 1
        for j in range(1,size):
            if nums[i] != nums[j]:
                nums[i+1] = nums[j]
                i += 1
            else:
                duplicate += 1
                
        return size-duplicate