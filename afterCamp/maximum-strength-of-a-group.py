class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        total = 0
        heap = []
        heapify(heap)
        for num in nums:
            if num > 0:
                if not total:
                    total = 1
                total *= num
            elif num < 0:
                heappush(heap,num)

        while len(heap) > 1:
            if not total:
                total = 1
            total *= heappop(heap)
            total *= heappop(heap)
        
        return total
