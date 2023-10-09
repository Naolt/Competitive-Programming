class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        grid = defaultdict(dict)
        cells = list(set(reduce(lambda x,y : x + y , equations)))

        for row in cells:
            grid[row] = {cell:inf for cell in cells}
        for index,[x,y] in enumerate(equations):
            grid[x][y] = values[index]
            grid[y][x] = 1/values[index]
        
        for row in cells:
            grid[row][row] = 1
        
        for k in cells:
            for row in cells:
                for col in cells:
                    if grid[row][k] * grid[k][col] < grid[row][col]:
                        grid[row][col] = grid[row][k] * grid[k][col]
        answer = []
        for x,y in queries:
            if x not in cells or y not in cells:
                answer.append(-1)
            else:
                answer.append(grid[x][y] if grid[x][y] != inf else -1)
        
        return answer