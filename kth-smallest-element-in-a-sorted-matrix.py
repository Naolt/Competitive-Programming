class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        result = []
        heap = []
        rowSize,colSize = len(matrix),len(matrix[0])

        for index,row in enumerate(matrix):
            heap.append((row[0],index,0))
        
        heapq.heapify(heap)
        
        while len(result) != k:
            val,r,c = heapq.heappop(heap)
            result.append(val)

            if c < colSize-1:
                heapq.heappush(heap,(matrix[r][c+1],r,c+1))
        
        return result[-1]