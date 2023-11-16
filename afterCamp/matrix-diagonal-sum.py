class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        size = len(mat)-1
        for i in range(size+1):
            total += mat[i][i]
            total += mat[i][size-i]
        
        if (size+1) % 2:
            total -= mat[size//2][size//2]

        return total 

"""
[7,3,1,9],
[3,4,6,9],
[6,9,6,6],
[9,5,8,5]]
"""