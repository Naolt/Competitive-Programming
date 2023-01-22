class Solution:
    
    def hasDuplicate(self,board,direction)->bool:
        # check duplicate value on each row
        if direction == 'row':
            for row in range(9):
                duplicateDict = {}
                for col in range(9):
                    if board[row][col] in duplicateDict:
                        return True
                    if board[row][col] != ".":
                        duplicateDict[board[row][col]] = 1
        else:
            for col in range(9):
                duplicateDict = {}
                for row in range(9):
                    if board[row][col] in duplicateDict:
                        return True
                    if board[row][col] != ".":
                        duplicateDict[board[row][col]] = 1
        return False
    
    
    def boxHasDuplicate(self,board,i,j)->bool:
        duplicateDict = {}
        
        for row in range(3):
            for col in range(3):
                if board[row+i][col+j] in duplicateDict:
                    return True
                if board[row+i][col+j] != ".":
                    duplicateDict[board[row+i][col+j]] = 1
        return False
            
            
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        if self.hasDuplicate(board,'row') or self.hasDuplicate(board,'col'):
            return False
        
        #if row and col has no duplicate check each box
        for row in range(0,9,3):
            for col in range(0,9,3):
                if self.boxHasDuplicate(board,row,col):
                    print(row,col)
                    return False
        return True
        