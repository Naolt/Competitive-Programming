class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        incoming = defaultdict(int)
        # recipesList = set(recipes)
        for index,ingredientList in enumerate(ingredients):
            for ingredient in ingredientList:
                graph[ingredient].append(recipes[index])
                incoming[recipes[index]] += 1
        
        queue = deque(supplies)
        result = []
        
        while queue:
            supply = queue.popleft()

            if supply in incoming:
                result.append(supply)
            for neighbour in graph[supply]:
                incoming[neighbour] -= 1

                if incoming[neighbour] == 0:
                    queue.append(neighbour)

        
        return result