class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        currMin = nums[0]
        

        for index,num in enumerate(nums):
            while stack and stack[-1][0] <= num:
                stack.pop()
            if stack and stack[-1][1] < num:
                return True
            stack.append((num,currMin))
            currMin  = min(currMin,num)
        return False