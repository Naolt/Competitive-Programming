from collections import defaultdict
n = int(input())
graph = defaultdict(list)
def addEdge(source,dest):
    graph[source].append(dest)
def Vertex():
    for key,values in graph.items():
        print(len(values),*sorted(values))

for i in range(n):
    row = list(map(int,input().split()))
    for index,val in enumerate(row):
        if val == 1:
            addEdge(i+1,index+1)
Vertex()

    
#5
#0 0 1 0 0
#1 0 1 0 0
#0 0 0 0 1
#1 1 0 0 0
#1 1 0 0 0
