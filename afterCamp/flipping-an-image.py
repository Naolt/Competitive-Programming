class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = []

        for i in range(len(image)):
            arr = []
            for j in range(len(image[0])-1,-1,-1):
                arr.append(1-image[i][j])
            result.append(arr)

        
        return result