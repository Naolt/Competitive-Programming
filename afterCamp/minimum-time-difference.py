class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        times = list(map(lambda x: tuple(map(int,x.split(':'))),timePoints))
        times.sort()
        def calcDiff(time1,time2):
            h1,m1 = time1
            h2,m2 = time2
            return 60*abs(h1-h2)+m2 - m1
        
        minDiff = inf

        for i in range(1,len(times)):
            minDiff = min(minDiff,calcDiff(times[i-1],times[i]))
            
        last = calcDiff((0,0),times[0]) + calcDiff(times[-1],(23,60))

        return min(minDiff,last)
