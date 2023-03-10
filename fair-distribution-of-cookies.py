class Solution:
    def __init__(self):
        self.minUnfairness = float('inf')
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        bucket = [0]*k
        self.backtrack(0,cookies,bucket)
        return self.minUnfairness

    def backtrack(self,idx,cookies,bucket):
        if idx >= len(cookies):
            self.minUnfairness = min(max(bucket),self.minUnfairness)
            return 

        size = len(cookies)
                
        for j in range(len(bucket)):
            bucket[j] += cookies[idx]
            if bucket[j] < self.minUnfairness:
                self.backtrack(idx+1,cookies,bucket[:])
            bucket[j] -= cookies[idx]
        
        return