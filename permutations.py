class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtrack(nums,[],0,result)
        return result
    def backtrack(self,nums,current,visited,result):
        size1 = len(current)
        size2 = len(nums)
        if size1 == size2:
            result.append(current[:])
            return
        
        for i in range(size2):
            # print(bin(visited),bool(visited & (1<<(nums[i]+10))),nums[i])
            if not (visited & (1<<(nums[i]+10))):
                current.append(nums[i])
                visited |= (1<<(nums[i]+10))
                self.backtrack(nums,current,visited,result)
                # print(current)
                current.pop()
                # print("removing",nums[i],bin(visited))
                # print(visited,(1<<(nums[i]+10)))
                visited -= (1<<(nums[i]+10))
                # print("after removing",nums[i],bin(visited),visited)
                # print(current)
        return