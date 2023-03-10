class Solution:
    def __init__(self):
        self.result = []
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.backtrack(1,[],k,n)
        return self.result

    def backtrack(self,idx,arr,k,n):
        if len(arr) == k:
            self.result.append(arr)
            return 
        if idx > n:
            return
        
        for i in range(idx,n+1):
            self.backtrack(i+1,arr+[i],k,n)