class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        cells = set()
        for x,y in equations:
            cells.add(x)
            cells.add(y)

        grid = defaultdict(dict)
        for cell in cells:
            grid[cell] = {c:float('inf') for c in cells}

        for index,(x,y) in enumerate(equations):
            grid[x][y] = values[index]
            grid[y][x] = 1/values[index]

        for k in cells:
            for row in cells:
                for col in cells:
                    grid[row][col] = min(grid[row][k]*grid[k][col],grid[row][col])

        result = []
        for x,y in queries:
            result.append(-1 if x not in cells or y not in cells or grid[x][y] == float('inf') else grid[x][y] )

        return result

        


