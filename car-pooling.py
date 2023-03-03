class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        maxKilometer = 0
        for trip in trips:
            maxKilometer = max(maxKilometer,trip[2])
        prefix = [0]*(maxKilometer+2)

        for [Num,From,To] in trips:
            prefix[From] += Num
            prefix[To] -= Num

        prefix = list(accumulate(prefix))
        if max(prefix) > capacity:
            return False
        else:
            return True