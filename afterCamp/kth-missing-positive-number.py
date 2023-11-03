class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        
        max_ = max(arr)
        arr = set(arr)
        size = max_ + k + 2
        for i in range(1,size+1):
            if i not in arr:
                k -= 1
            if k == 0:
                return i
                


