from collections import defaultdict
n = int(input())
graph = defaultdict(list)
grid = []
for i in range(1,n+1):
    grid.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            graph[i].append(j)
            grid[j][i] = 0
result = 0
for key,values in graph.items():
    result += len(values)
print(result)

