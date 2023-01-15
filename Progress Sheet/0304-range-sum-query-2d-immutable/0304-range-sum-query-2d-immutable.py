class NumMatrix(object):
    def __init__(self, matrix):
        rows,cols=len(matrix),len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if j!=0:
                    matrix[i][j]+=matrix[i][j-1]
                if i!=0 :
                    matrix[i][j]+=matrix[i-1][j]
                if i!=0 and j!=0:
                    matrix[i][j]-=matrix[i-1][j-1]
        self.matrix=matrix
    def sumRegion(self, row1, col1, row2, col2):
        region=self.matrix[row2][col2]
        if col1!=0:
            region-=self.matrix[row2][col1-1]
        if row1!=0:
            region-=self.matrix[row1-1][col2]
        if row1!=0 and col1!=0:
            region+=self.matrix[row1-1][col1-1]
        return region