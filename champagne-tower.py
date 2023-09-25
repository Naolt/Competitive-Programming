class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        if poured == 0:
            return float(0)

        tower = [[float(0)]*100 for i in range(100)]

        tower[0][0] = poured

        
        for row in range(min(query_row+1,99)):
            
            for col in range(100):
                if tower[row][col] > 1:
                    leftOver = float(tower[row][col]-1)
                    tower[row][col] = 1
                    tower[row+1][col] += (leftOver/2)
                    tower[row+1][col+1] += (leftOver/2)

        return tower[query_row][query_glass]