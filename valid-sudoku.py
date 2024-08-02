class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def checkRows():
            for row in board:
                dic = defaultdict(int)
                for val in row:
                    if val != '.':
                        if val in dic:
                            return False
                        dic[val] += 1
            return True
        def checkCols():
            for col in range(9):
                dic = defaultdict(int)
                for row in range(9):
                    val = board[row][col]
                    if val != ".":
                        if val in dic:
                            return False
                        dic[val] += 1
            return True

        def checkBoxes():

            for i in range(3):
                for j in range(3):
                    dic = defaultdict(int)
                    for k in range(3):
                        for l in range(3):
                            val = board[k+(i*3)][l+(j*3)]
                            if val != ".":
                                if val in dic:
                                    return False
                            dic[val] += 1
            return True
        
        return checkRows() and checkCols() and checkBoxes()