class Solution:
    def checkStraightLine(self,  c: List[List[int]]) -> bool:
        x1,y1 = c[0]
        x2,y2 = c[1]
        slope = (y2-y1)/(x2-x1) if x2-x1 != 0 else "a"
        for i in range(2,len(c)):
            x2,y2 = c[i] 
            s = (y2-y1)/(x2-x1) if x2-x1 != 0 else "a"
            if slope != s:
                return False


        return True
