class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
       
        window_start = 0
        max_so_far = 0
        fruit_basket = {}
        for window_end in range(len(fruits)):
            right_fruit = fruits[window_end]
            if right_fruit not in fruit_basket:
                fruit_basket[right_fruit] = 1
            else:
                fruit_basket[right_fruit] += 1
            while len(fruit_basket) > 2:
                left_fruit = fruits[window_start]
                fruit_basket[left_fruit] -= 1
                if fruit_basket[left_fruit] == 0:
                    del fruit_basket[left_fruit]
                window_start += 1
            max_so_far = max(max_so_far, window_end - window_start+1)
        return max_so_far
