class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack(0,nums,[],set(),result)
        return result
    def backtrack(self,idx,nums,current,visited,result):
        size1 = len(current)
        size2 = len(nums)
        if size1 == size2:
            result.append(current[:])
            return
        
        for i in range(size2):
            if nums[i] not in visited:
                current.append(nums[i])
                visited.add(nums[i])
                self.backtrack(i+1,nums,current,visited,result)
                current.pop()
                visited.remove(nums[i])
        return