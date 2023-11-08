class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        monotone = defaultdict(int)
        monotoneRev = defaultdict(int)
        stack = []
        
        for num in nums:
            while stack and stack[-1] < num:
                monotone[stack.pop()] = num
            stack.append(num)
        
        stack2 = []
        for num in nums[::-1]:
            while stack2 and stack2[-1] < num:
                monotoneRev[stack2.pop()] = num
            stack2.append(num)

        return not monotone or not monotoneRev

        