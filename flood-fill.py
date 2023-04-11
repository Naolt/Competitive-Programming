class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        prev = image[sr][sc] 
        # image[sr][sc] = color
        if color != prev:
            self.fill(image,sr,sc,color,prev)
        return image
    def fill(self,image,sr,sc,color,prevColor):
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        if (not self.inBound(sr,sc,image)) or image[sr][sc] != prevColor:
            return
        if image[sr][sc] == prevColor: 
            image[sr][sc] = color
        for r,c in directions:
            row = sr + r
            col = sc + c
            self.fill(image,row,col,color,prevColor)
        return
    def inBound(self,x,y,image):
        return (0 <= x < len(image)) and (0 <= y < len(image[0]))