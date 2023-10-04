def bellman(src):
    n,m = map(int,input().split())
    graph = []
    
    for _ in range(m):
        graph.append(list(map(int,input().split())))
    dist = [float('inf')]*n
    dist[src-1] = 0
    for _ in range(n-1):
        for u,v,w in graph:
            if dist[u-1] != float('inf') and dist[u-1] + w < dist[v-1]:
                dist[v-1] = dist[u-1] + w
    result = []
    for num in dist:
        if num == float('inf'):
            result.append(30000)
        else:
            result.append(num)

    return result


print(*bellman(1))
