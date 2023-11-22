class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        

        @cache
        def getCount(num):
            if num == 1:
                return 0
            if num % 2 == 0:
                return 1 + getCount(num//2)
            else:
                return 1 + getCount(3*num+1)

        nums = []

        for num in range(lo,hi+1):
            nums.append((getCount(num),num))
        
        nums.sort()

        return nums[k-1][1]
        