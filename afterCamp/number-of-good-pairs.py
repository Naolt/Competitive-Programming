class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        numDict = defaultdict(int)
        answer = 0

        for num in nums:
            answer += numDict[num]
            numDict[num] += 1
        
        return answer

