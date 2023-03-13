class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 0
        right = max(nums)+1

        while left+1 < right:
            middle = left + (right - left)//2
            print("answer: ",self.divide(nums,middle),left,middle,right)
            if self.divide(nums,middle) > threshold:
                left = middle
            else:
                right = middle 
        return left+1

    def divide(self,nums,k):
        total = 0
        for num in nums:
            total += math.ceil(num/k)
        return total