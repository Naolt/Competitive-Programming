class Solution:
    def move(self,matrix,i,j,rotationCount,size):
        if rotationCount == 4:
            return
        elem = matrix[i][j]
        self.move(matrix,j,size-1-i,rotationCount+1,size)
        matrix[j][size-1-i] = elem
    
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        
        for level in range(size//2):
            for j in range(level,size-1-level):
                self.move(matrix,level,j,0,size)
		
		
    
	
		