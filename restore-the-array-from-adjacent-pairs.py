class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incoming = defaultdict(int)
        for start,end in adjacentPairs:
            graph[start].append(end)
            graph[end].append(start)
            incoming[start] += 1
            incoming[end] += 1

        queue = deque()
        topSortedList = []

        for key,value in incoming.items():
            if value == 1:
                queue.append(key)
        
        while queue:
            leaf = queue.popleft()
            topSortedList.append(leaf)
            
            for nbr in graph[leaf]:
                incoming[nbr] -= 1

                if incoming[nbr] == 1:
                    queue.append(nbr)
        
        result = [0]*len(incoming)
        i = 0
        j = len(result)-1
        turn = True

        for num in topSortedList:
            if turn:
                result[i] = num
                i += 1
            else:
                result[j] = num
                j -= 1
            
            turn = not turn
        return result