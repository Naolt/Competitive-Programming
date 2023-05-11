from typing import List
from collections import defaultdict
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		colors = [0]*V
		graph = defaultdict(list)
		for index,values in enumerate(adj):
		    graph[index] = values
		    
		for i in range(V):
		    if self.hasCycle(i,graph,colors,-1):
		        return 1
		return 0
        
        
    def hasCycle(self,current,graph,colors,prev):
        if colors[current] == 2:
            return False
        
        if colors[current] == 1:
            return True
        
        colors[current] = 1
        for neighbour in graph[current]:
            if neighbour != prev:
                cycleFound = self.hasCycle(neighbour,graph,colors,current)
                if cycleFound:
                    return True
        colors[current] = 2  
        return False

#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends