# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        size = mountain_arr.length()
        left = 0
        right = size-1
        mountain = 0
        while left <= right:
            mid = left + (right - left) // 2
            l = -float(inf) if mid == 0 else mountain_arr.get(mid-1)
            m = mountain_arr.get(mid)
            r = mountain_arr.get(mid+1)
            
            if l < m > r:
                mountain = mid
                break
            elif m < r:
                left = mid + 1
            else:
                right = mid - 1
    
        
        def binary_inc(start,end,inc):
            left = start
            right = end

            while left <= right:
                mid = left + (right - left) // 2
                m = mountain_arr.get(mid)

                if m == target:
                    return mid
                elif (inc and m < target) or (not inc and m > target):
                    left = mid + 1
                else:
                    right = mid - 1

            return -1

        leftFound = binary_inc(0,mountain,True)
        if leftFound  > -1:
            return leftFound
    
        return binary_inc(mountain,size-1,False)