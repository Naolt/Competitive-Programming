class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        size = len(nums)

        @cache
        def findScore(mask,n):
            
            maxGcd = 0
            for i in range(size):
                for j in range(i+1,size):
                    if (mask >> i) &  1 or (mask >> j) & 1:
                        continue
                    mask |= (1 << i)
                    mask |= (1 << j)
                    result = findScore(mask,n+1) + n*gcd(nums[i],nums[j])
                    maxGcd = max(maxGcd,result)
                    mask ^= (1 << i)
                    mask ^= (1 << j)
                
            return maxGcd
        
        return findScore(0,1)