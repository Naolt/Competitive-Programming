class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total = (n-1)+(m-1)
        return factorial(total)//(factorial(total-(m-1))*(factorial(m-1)))