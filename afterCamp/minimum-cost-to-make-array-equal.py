class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        arr = list(zip(nums,cost))
        arr.sort()

        def calcCost(x):
            return sum(abs(x-n)*c for n,c in arr)

        left = arr[0][0]
        right = arr[-1][0]
        val = calcCost(left)

        while left <= right:

            mid = left + (right-left)//2
            cm1,cm2 = calcCost(mid),calcCost(mid+1)
            val = min(cm1,cm2)
            if cm1 > cm2:
                left = mid + 1
            else:
                right = mid - 1

        return val
      
