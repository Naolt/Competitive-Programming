from sortedcontainers import SortedSet

class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        mySet = SortedSet()
        currMin = inf

        for index in range(x,len(nums)):
            value = nums[index]
            if value in mySet:
                return 0

            mySet.add(nums[index-x])
            right = min(bisect_right(mySet,nums[index]),len(mySet)-1)
            left = max(right-1,0)
            currMin = min(currMin,abs(mySet[left]-value),abs(mySet[right]-value))

        return currMin
