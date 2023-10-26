class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        maxN = max(nums)
        minN = min(nums)
        avg = (minN+maxN)/2
        num = min(avg,k)
        newMax = maxN-num if maxN-num >= avg else num 
        newMin = minN+num if minN+num <= avg else num 
        return int(newMax - newMin)