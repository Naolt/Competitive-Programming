class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        def customSort(nums):

            for i in range(1,len(nums)):
                curr = nums[i]

                for j in range(i,0,-1):
                    if nums[j] > nums[j-1]:
                        nums[j],nums[j-1] = nums[j-1],nums[j]
                    else:
                        break
                
        
        zipped_list = list(zip(heights,names))
        customSort(zipped_list)

        return [name for _,name in zipped_list]
