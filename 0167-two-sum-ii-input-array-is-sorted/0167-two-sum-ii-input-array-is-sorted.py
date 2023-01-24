class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        
        while left < right:
            addition = numbers[left] + numbers[right]
            if addition == target:
                return [left+1,right+1]
            elif addition < target:
                left += 1
            else:
                right -= 1
                
        