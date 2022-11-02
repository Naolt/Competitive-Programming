class Solution(object):
	def pivotIndex(self, nums):
		totalSum = 0 
		leftSum = 0 
		for num in nums:
			totalSum +=num
		for e in range(len(nums)):
			if(totalSum - leftSum - nums[e] == leftSum):
				return e
			leftSum += nums[e]
		return -1;
