T = int(input())





for i in range(T):
    # for diagonal 1
    d1 = {}
    # for diagonal 2
    d2 = {}
    board = []
    totalMax = 0
    
    [rowSize,colSize] = list(map(int,input().split()))
    
    for row in range(rowSize):
        numList = list(map(int,input().split()))
        board.append(numList)
        
        
    
    for row in range(rowSize):
        
        for col in range(colSize):
            xsum = 0
            if row-col in d1:
                xsum += d1[row-col]
            else:
                i = row
                j = col
                diagonalSum = 0
                while 0 <= i < rowSize and 0 <= j < colSize:
                    diagonalSum += board[i][j]
                    i += 1
                    j += 1
                d1[row-col] = diagonalSum
                xsum += diagonalSum
            
            if row+col in d2:
                xsum += d2[row+col]
            else:
                i = row
                j = col
                diagonalSum = 0
                while 0 <= i < rowSize and 0 <= j < colSize:
                    diagonalSum += board[i][j]
                    i += 1
                    j -= 1
                d2[row+col] = diagonalSum
                xsum += diagonalSum
            xsum -= board[row][col]
        
            totalMax = max(totalMax,xsum)
        
    print(totalMax)
            
"""
time Complexity = O(n*m*n)
space Complexity = O(max(m,n)/2) = max(m,n)
"""
                    
            
    
