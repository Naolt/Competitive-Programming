class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        self.backtrack(0,0,nums,dic,[])
        return dic[max(dic)]

    def backtrack(self,idx,current,nums,dic,comb):
        size = len(nums)
        dic[current] += 1
        if idx >= size:
            return
        for i in range(idx,len(nums)):
            comb.append(nums[i])
            self.backtrack(i+1,current|nums[i],nums,dic,comb)
            comb.pop()