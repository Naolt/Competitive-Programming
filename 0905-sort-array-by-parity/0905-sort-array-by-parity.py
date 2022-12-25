class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        size = len(nums)
        for i in range(size):
            print(nums[i]/2)
            if nums[i]%2 == 0:
                nums.insert(0,nums[i])
                nums.pop(i+1)
        return nums
                