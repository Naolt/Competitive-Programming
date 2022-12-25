"""
[0,0,1,3,2,2,3,4,5,6], val = 2
[3,3,2,2] 3 
 i
 j

approach
 - sort the array in decending order then find the first occurence of the element



"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums.sort(reverse=True)
        minIndex = 0
        freq = 0
        if(val in nums):
            minIndex = nums.index(val)
            freq = nums.count(val)
        
        for i in range(freq):
            nums[minIndex+i] = 0
        nums.sort(reverse=True)
        return len(nums)-freq
        