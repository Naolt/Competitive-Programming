class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        intials = []
        for index,[start,end] in enumerate(intervals):
            intials.append((start,index))
        intials.sort()

        result = []
        for start,end in intervals:
            index = self.getIndex(intials,end)
            if index == -1:
                result.append(intials[0][1])
            elif index == len(intials):
                result.append(-1)
            else:
                result.append(intials[index][1])
        return result
    def getIndex(self,nums,target):
        left = -1
        right = len(nums)

        while left+1 < right:
            middle = left + (right-left)//2

            if nums[middle][0] < target:
                left = middle
            else:
                right = middle
        return left+1