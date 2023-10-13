"""
size = 5
[8,5,9,9,8,4]
[4,5,8,8,9,9]
 
"""



class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        size = len(nums)
        nums.sort()
        maxGap,dup,start = 0,0,0

        prefix = [0]*(size+1)
        visited = set()
        visited.add(nums[0])
        for i in range(1,size):
            if nums[i] in visited:
                prefix[i] = 1
            visited.add(nums[i])
        prefix = list(accumulate(prefix))


        for index,num in enumerate(nums):
            expected = num + (size-1)
            bound = bisect_left(nums,expected)
            if bound == size:
                bound = size-1
            if nums[bound] > expected:
                bound -= 1
            if maxGap-dup < (bound-index)-(prefix[bound]-prefix[index]):
                maxGap = bound-index
                start = index
                dup = prefix[bound]-prefix[index]
        
        return (size-(maxGap+1)) + dup