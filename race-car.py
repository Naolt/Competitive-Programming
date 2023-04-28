class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0,1)])
        visited = set([(0,1)])
        def getSign(num):
            return 1 if num < 0 else -1

        count = 0
        while queue:
            size = len(queue)
            # print(queue)
            for i in range(size):
                pos,speed = queue.popleft()

                if pos == target:
                    return count

                if  (pos,getSign(speed)) not in visited:
                    queue.append((pos,getSign(speed)))
                    visited.add((pos,getSign(speed)))
                if (pos + speed,speed*2) not in visited:
                    queue.append((pos + speed,speed*2))
                    visited.add((pos + speed,speed*2))
                
            count += 1