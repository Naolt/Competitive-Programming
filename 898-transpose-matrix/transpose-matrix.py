class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        trans = [ [0]*len(matrix) for col in range(len(matrix[0]))]

        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                trans[col][row] = matrix[row][col]


        return trans
        