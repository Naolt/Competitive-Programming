class Solution:
    def __init__(self):
        self.memo = {}
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.dp(nums,0,target,0)


    def dp(self,nums,idx,target,total):
        if idx == len(nums):
            if total == target:
                return 1
            return 0
        
        if (idx,total) in self.memo:
            return self.memo[(idx,total)]

        pos = self.dp(nums,idx+1,target,total+nums[idx])
        neg = self.dp(nums,idx+1,target,total-nums[idx])

        self.memo[(idx,total)] = pos + neg

        return pos + neg