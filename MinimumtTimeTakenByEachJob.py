from typing import List
from collections import defaultdict
from collections import deque

from typing import List


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        
        graph = defaultdict(list)
        incoming = [0]*n
        result = [0]*n
        
        for start,end in edges:
            graph[start].append(end)
            incoming[end-1] += 1
        
        queue = deque()
        
        for key,val in enumerate(incoming):
            if val == 0:
                queue.append(key+1)
        
        # print(queue)
        count = 1
        while queue:
            size = len(queue)
            for i in range(size):
                popped = queue.popleft()
                result[popped-1] = str(count)
                
                for nbr in graph[popped]:
                    
                    incoming[nbr-1] -= 1
                    if incoming[nbr-1] == 0:
                        queue.append(nbr)
            count += 1
        
        # print(result)
        
                
        return " ".join(result)



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        print(res)
        

# } Driver Code Ends