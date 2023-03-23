class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = defaultdict(int)
        self.backtrack(nums,[],0,result)
        return result 
    def backtrack(self,nums,bucket,idx,result):
        size = len(nums)
        if idx >= size or len(bucket) >= 2:
            if len(bucket) >= 2:
                result[tuple(bucket[:])] += 1
            if idx >= size:
                print(idx,bucket)
                return         
        for i in range(idx,size):
            if not bucket or bucket[-1] <= nums[i]:
                bucket.append(nums[i])
                self.backtrack(nums,bucket,i+1,result)
                bucket.pop()