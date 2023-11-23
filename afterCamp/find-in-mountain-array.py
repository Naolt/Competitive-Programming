# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        

        def getPivot():
            left = 0
            right = mountain_arr.length()-1

            while left <= right:
                mid = left + (right-left)//2
                
                midVal = mountain_arr.get(mid) 
                midNext = mountain_arr.get(mid+1)

                if midVal <= midNext:
                    left = mid+1
                else:
                    right = mid-1
            
            return left
        
        pivot = getPivot()

        # search in left sub array
        left = 0
        right = pivot

        while left <= right:
            mid = left + (right-left)//2
            midVal = mountain_arr.get(mid) 

            if midVal == target:
                return mid
            elif midVal < target:
                left = mid+1
            else:
                right = mid-1
        
         # search in right sub array
        left = pivot+1
        right = mountain_arr.length()-1

        while left <= right:
            mid = left + (right-left)//2
            midVal = mountain_arr.get(mid) 

            if midVal == target:
                return mid
            elif midVal > target:
                left = mid+1
            else:
                right = mid-1
        



        return -1
                    


        