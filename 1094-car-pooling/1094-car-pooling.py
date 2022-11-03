class Solution(object):
    def carPooling(self, trips, capacity):
        stops = [0 for i in range(1001)]
        for i in trips:
            stops[i[1]]+=i[0]
            stops[i[2]]-=i[0]
        for i in stops:
            capacity-=i
            if capacity<0:
                return False
        return capacity>=0
        