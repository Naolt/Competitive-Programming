class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str,nums))
        size = len(nums)
        for i in range(size):
            for j in range(size-1):
                #if the last number is 0 
                post = nums[j] + nums[j+1]
                pre = nums[j+1] + nums[j]
                if int(pre) > int(post):
                    nums[j],nums[j+1] = nums[j+1],nums[j]
                    
                        
        if nums[0] == "0":
            for i in range(1,size):
                if nums[i] == "0":
                    nums[i] = ''
                else:
                    break
                
        return "".join(nums)
                        
                    
        
        