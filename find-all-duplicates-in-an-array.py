class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        size = len(nums)
        i,result = 0, []
        while i < size:
            position = nums[i]-1
            if i != position and nums[position] != nums[i]:
               nums[i],nums[position] = nums[position],nums[i]
            else:
                i += 1
        for j in range(size):
            if nums[j]-1 != j:
                result.append(nums[j])
        return result