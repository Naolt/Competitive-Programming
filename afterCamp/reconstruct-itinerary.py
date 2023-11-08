class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        tickets = list(map(tuple,tickets))
        tickets.sort(reverse=True)
        for index,[start,end] in enumerate(tickets):
            graph[start].append(end)
        
        stack = ['JFK']
        route = []
        while stack:
            start = stack[-1]
            if len(graph[start]):
                stack.append(graph[start].pop())
            else:
                route.append(stack.pop())
            
        return route[::-1]

        
        
        
        
        
        
       


                    


            

