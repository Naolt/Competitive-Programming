class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        count = 0

        for char in s:
            if char == "(":
                stack.append(count)
                count = 0
            else:
                if count == 0:
                    count = 1
                else:
                    count *= 2
                count += stack.pop()
        return count