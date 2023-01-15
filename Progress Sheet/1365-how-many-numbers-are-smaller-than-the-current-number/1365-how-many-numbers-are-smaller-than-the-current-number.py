class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        n = len(nums)
        output = [0]*n
        for i in range(n):
            for j in range(n):
                if(nums[i]>nums[j]):
                    output[i]+=1
        return output
        