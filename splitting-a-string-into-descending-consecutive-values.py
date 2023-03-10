class Solution:
    def splitString(self, s: str) -> bool:
        return self.backtrack(0,[],s,len(s))
    def backtrack(self,idx,arr,s,n):
        if idx >= len(s):
            return len(arr) >= 2
        
        for i in range(idx,n):
            val = int(s[idx:i+1])
            if not arr or arr[-1] - 1 == val:
                arr.append(val)
                if self.backtrack(i+1,arr[:],s,n):
                    return True
                arr.pop()

        return False