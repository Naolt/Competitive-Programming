class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        #sort by grow time
        sortedGrow = []
        for i,num in enumerate(growTime):
            sortedGrow.append(tuple([num,i]))
            
        sortedGrow.sort()
        print(sortedGrow)
        
        sortedNum = sorted(sortedGrow,reverse=True)
        print(sortedNum)
        
        total = 0
        planting = 0
        
        for time,index in sortedNum:
            pandg = time + plantTime[index]
            if  pandg > total - planting:
                total += (pandg - (total - planting)) 
                planting += plantTime[index]
            else:
                planting += plantTime[index]
        return total
                