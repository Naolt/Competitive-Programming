class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for astr in asteroids:
            if astr < 0:
                while stack and stack[-1] > 0 and -stack[-1] > astr:
                    stack.pop()
                if not stack:
                    stack.append(astr)
                elif -stack[-1] == astr:
                    stack.pop()
                elif stack[-1] < 0:
                    stack.append(astr)
            else:
                stack.append(astr)

        return stack

