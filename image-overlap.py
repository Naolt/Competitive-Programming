class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:

        size = len(img1)
        add = 2*(size-1)
        cSize = size + add
        box = [[0]*cSize for i in range(cSize)]

        for i in range(size):
            for j in range(size):
                box[i+size-1][j+size-1] = img1[i][j]
        
        max_ = 0
        for i in range(cSize-(size-1)):
            for j in range(cSize-(size-1)):
                count = 0
                for row in range(size):
                    for col in range(size):
                        if img2[row][col] and box[row+i][col+j]:
                            count += 1
                max_ = max(max_,count)

        return max_