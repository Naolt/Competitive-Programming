class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.xCords = defaultdict(set)
        self.yCords = defaultdict(set)

    def add(self, point: List[int]) -> None:
        x,y = point
        self.points[(x,y)] += 1
        self.xCords[x].add((x,y))
        self.yCords[y].add((x,y))
        

    def count(self, point: List[int]) -> int:
        sx,sy = point
        total = 0
        for x,y in self.xCords[sx]:
            if sy == y: continue
            distance = self.distance(point,[x,y])
            for i,j in self.yCords[sy]:
                if distance == self.distance(point,[i,j]) and (i,y) in self.points:
                    prod = self.points[(x,y)] * self.points[(i,j)] * self.points[(i,y)]
                    total += prod
        return total 


    
    def distance(self,point1,point2):
        x1,y1 = point1
        x2,y2 = point2
        return  math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)