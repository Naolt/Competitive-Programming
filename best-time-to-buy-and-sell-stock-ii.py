class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        numDict = defaultdict(list)

        stack = []
        for index,price in enumerate(prices):

            if not stack or stack[-1][0] > price:
                stack.append((price,index))
            else:
                while stack and stack[-1][0] < price:
                    numDict[stack.pop()].append((price,index))
                stack.append((price,index))
        total = 0
        used = set()
        for key,value in numDict.items():
            
            if value[-1] not in used:
                total += (value[-1][0]-key[0])
                used.add(value[-1])
        return total