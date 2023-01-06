from collections import deque

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        
        answer = deque([])
        
        #calculate sum of even intially
        sumOfEven = 0
        for num in nums:
            if num % 2 == 0:
                sumOfEven +=num
        answer.append(sumOfEven)
        
        for [val,index] in queries:
            lastValue = answer[-1]
            newValue = nums[index] + val
            
            #if number is even substract it from the last element in the list
            if nums[index] % 2 == 0:
                lastValue = lastValue - nums[index]
            if newValue % 2 == 0:
                answer.append(newValue+lastValue)
            else:
                answer.append(lastValue)
            nums[index] = newValue
        answer.popleft()
        return answer
                
            
        