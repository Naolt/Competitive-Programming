class Solution:
    
    def sum(self,num)->int:
        return num+1
    def sub(self,num)->int:
        return num-1
    def doNothing(self,num)->int:
        return num
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        
        opDict = {"+":self.sum,"-":self.sub,"=":self.doNothing}
        paths = ["++","--","+-","-+","+=","-=","=-","=+"]
        queenList = set(map(tuple,queens))
        result = []
        
       
        for path in paths:
            opX = path[0]
            opY = path[1]
            
            row = king[0];
            col = king[1]
            
            
            while( 0 <= row < 8 and 0 <= col < 8  ):
                
                row = opDict[opX](row)
                col = opDict[opY](col)
                print(row,col,opX,opY)
                if (row,col) in queenList:
                    result.append([row,col])
                    break
        return result
            
            
                
                
                
            
            
        