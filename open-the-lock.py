class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set()
        for deadend in deadends:
            visited.add(deadend)
        if '0000' in visited:
            return -1
        queue = deque([[0,0,0,0]])
        count = 0
        while queue:
            size = len(queue)
            for i in range(size):
                currentState = queue.popleft()
                newState = list(map(str,currentState))
                stringified = "".join(newState)
                if stringified == target:
                    return count
                possibleStates = self.getMoves(currentState)
                for state in possibleStates:
                    newState = list(map(str,state))
                    stringified = "".join(newState)
                    # if stringified == target:
                        # return count
                    if stringified not in visited:
                        queue.append(state)
                        visited.add(stringified)
            count += 1
                # print(visited)
        return -1

    def getMoves(self,state):
        result = []
        for i in range(4):
            state[i] += 1
            state[i] %= 10
            result.append(state[:])

            state[i] -= 2
            state[i] %= 10
            result.append(state[:])
            
            state[i] += 1
            state[i] %= 10
        return result