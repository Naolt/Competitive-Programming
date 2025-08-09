class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:

        zeros = [0]*(len(nums)+1)
        ones = [0]*(len(nums)+1)

        for i,val in enumerate(nums):
            zeros[i+1] = zeros[i] + (1-val)
        
        for i in range(len(nums)-1,-1,-1):
            ones[i] = ones[i+1] + nums[i]

        res = []
        max_score = 0

        for i in range(len(nums)+1):
            score = zeros[i] + ones[i]
            if score > max_score:
                max_score = score
                res = [i]
            elif score == max_score:
                res.append(i)
            
        return res
            