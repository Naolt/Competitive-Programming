class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        
        piles = 3,6,7,11

        Approach 1: Binary search
        - choose k to be the max pile 
        - try minimizing k using binary search

        time: 10 ^ 4 log 10 ^ 9
        space: n

        """

        def canEat(newK):
            timeElapsed = 0

            for pile in piles:
                timeElapsed += ceil(pile / newK)

            return timeElapsed <= h

        low = 1
        high = max(piles)

        while low < high:
            mid = low + (high - low)//2

            if canEat(mid):
                high = mid
            else:
                low = mid + 1 

        return low