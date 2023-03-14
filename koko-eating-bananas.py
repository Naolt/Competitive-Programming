class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 0
        right = max(piles)+1

        while left+1 < right:
            middle = math.ceil(left + (right-left)/2)
            print(left,middle,right,self.getHours(piles,middle))
            if self.getHours(piles,middle) <= h:
                right = middle
            else:
                left = middle
        return left+1


    def getHours(self,piles,k):
        hours = 0
        for pile in piles:
            temp = pile/k
            if temp <= 0:
                hours += 1
            else:
                hours += math.ceil(temp)
        return hours