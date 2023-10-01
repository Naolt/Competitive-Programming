class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:

        maxXor = 0
        mask = 0

        for i in range(31,-1,-1):
            mask |= (1 << i)

            selected = set()
            for num in nums:
                selected.add( num & mask )
            
            temp = maxXor | (1 << i)
            
            for num in selected:
                if num ^ temp in selected:
                    maxXor = temp
                    break
        
        return maxXor