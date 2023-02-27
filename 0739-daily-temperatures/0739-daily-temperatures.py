class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        valueDict = collections.defaultdict(lambda:0)
        size = len(temperatures)
        for index,num in enumerate(temperatures):
            while stack and stack[-1][0] < num:
                ans = stack.pop()
                valueDict[ans] = index-ans[1]
            stack.append((num,index))
            
        for i in range(size):
            temperatures[i] = valueDict[(temperatures[i],i)]
        return temperatures