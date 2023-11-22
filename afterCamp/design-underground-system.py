class UndergroundSystem:

    def __init__(self):
        self.log = defaultdict(lambda: [0,0])
        self.checkIns = defaultdict(int)
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkIns[id] = [t,stationName]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        time,checkInStation = self.checkIns[id]
        total,count = self.log[(checkInStation,stationName)]
        self.log[(checkInStation,stationName)] = [total+(t-time),count+1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total,count = self.log[(startStation,endStation)]
        return total/count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)