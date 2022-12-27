class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        size = len(nums)
        i = 0
        
        
        while(i < size):
            j = size-1
            while i!= j:
                if(nums[i] == nums[j]):
                    count += 1
                j -= 1
            i+=1
        return count
        
