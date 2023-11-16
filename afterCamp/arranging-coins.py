class Solution:
    def arrangeCoins(self, n: int) -> int:

        root = sqrt((2*n-1)*4+1)//2
        summation = root*(root+1)//2

        if summation == n:
            return int(root)
        elif summation < n:
            return int(root)
        else:
            return int(root-1)

        