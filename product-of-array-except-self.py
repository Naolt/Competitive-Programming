class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        prefixProduct = [1]*size
        postfixProduct = [1]*size
        for i in range(1,size):
            prefixProduct[i]= prefixProduct[i-1]*nums[i-1]
        for i in range(size-2,-1,-1):
            postfixProduct[i] = postfixProduct[i+1]*nums[i+1]
        for i in range(size):
            prefixProduct[i] = prefixProduct[i]*postfixProduct[i]
        return prefixProduct