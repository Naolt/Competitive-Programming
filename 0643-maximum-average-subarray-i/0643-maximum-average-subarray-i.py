class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        window = nums[:k]
        size = len(nums)
        maxSum = float('-inf')
        currentSum = sum(window) - nums[k-1] 
        for i in range(k-1,size):
            currentSum += nums[i]
            maxSum = max(currentSum,maxSum)
            currentSum -= nums[i-k+1]
        return maxSum/k
            
        