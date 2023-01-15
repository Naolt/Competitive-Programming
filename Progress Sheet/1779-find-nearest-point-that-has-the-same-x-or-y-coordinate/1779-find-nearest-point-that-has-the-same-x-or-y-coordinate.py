"""
 x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
                                      i    
 
 smallestIndex = 2
 
 
 approach:
  - in order to be candidate for further calculation checking the point should match  with x or y
  - if a candidate isn't found return -1
  - else calculate the manhatan distance for each candidate point and index of it on variable and if            other point with same manhatan distance is found later skip it if smaller is found replace the            index
  
  



"""


class Solution(object):
    def calcManhatan(self,list1,list2):
        result = abs(list1[0]-list2[0]) + abs(list1[1]-list2[1])
        return result
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        size = len(points)
        smallestIndex = -1
        
        for i in range(size):
            if points[i][0] == x or points[i][1] == y:
                if smallestIndex == -1:
                    smallestIndex = i
                else:
                    if self.calcManhatan([x,y],points[smallestIndex]) > self.calcManhatan([x,y],points[i]):
                        smallestIndex = i
        return smallestIndex
                
    