class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = collections.defaultdict(int)
        left = 0
        size = len(fruits)
        result = 0
        
        for i in range(size):
            basket[fruits[i]] += 1
            
            if len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
            
            result = max(result,i-left+1)

        return result