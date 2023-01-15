class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row = 0
        col = 0
        up = False
        rowSize = len(mat)
        colSize = len(mat[0])
        diagonal = [mat[row][col]]
        
        halfwayup = False
        halfwaydown = False
        
        if(rowSize ==1 or colSize == 1):
            if rowSize == 1:
                for i in range(1,colSize):
                    diagonal.append(mat[0][i])
            else:
                for i in range(1,rowSize):
                    diagonal.append(mat[i][0])
            return diagonal
        
        while row != rowSize or colSize != colSize:
            # print(halfway)
            if up == False: 
                if halfwayup:
                    row += 1
                else:
                    col += 1
                while col >= 0 and row < rowSize:
                    print("going down",halfwayup,row,col)
                    diagonal.append(mat[row][col])
                    
                    row += 1
                    col -= 1
                up = True
                row -= 1
                col += 1
            else:
                if halfwaydown:
                    col += 1
                else:
                    row += 1
                while row >= 0 and col < colSize:
                    print("going up",halfwaydown,row,col)
                    diagonal.append(mat[row][col])
                    
                    row -= 1
                    col += 1
                up = False
                row += 1
                col -= 1
            
            
            if (up == False and row >= 0 and col == colSize-1) or (up == True and row == rowSize-1 and col >= 0) :
                # print("halfway",row,col)
                if up == False and row >= 0 and col == colSize-1:
                    halfwayup = True
                else:
                    halfwaydown = True
            else:
                pass
                # print("not halfway",row,col)
                    
        return diagonal
                