class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set([0])
        size = len(rooms)
        queue = deque([0])

        while queue:
            keys = rooms[queue.popleft()]
            for key in keys:
                if key not in visited:
                    queue.append(key)
                    visited.add(key)
        return size == len(visited)