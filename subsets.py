class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.getSubsets(0,[],nums,result)
        return result
    def getSubsets(self,idx,arr,nums,result):
        if idx >= len(nums):
            result.append(arr[:])
            return

        arr.append(nums[idx])
        self.getSubsets(idx+1,arr,nums,result)
        arr.pop()
        self.getSubsets(idx+1,arr,nums,result)