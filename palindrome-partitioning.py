class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        result = []
        def backtrack(w,path):
            if len(w) == 0:
                result.append(path[:])
                return
    
            for i in range(1,len(w)+1):
                cur = w[:i]
                if cur == cur[::-1]: 
                    backtrack(w[i:],path+[cur])
        
        backtrack(s,[])
        return result