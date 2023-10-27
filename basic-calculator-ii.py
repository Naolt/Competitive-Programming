class Solution:
    def calculate(self, s: str) -> int:
        # space removed and calculate multiplication and div
       
        signs = set(['+','-','/','*'])
        stack = []
        i = 0

        while i < len(s):
            char = s[i]
            if char == " ":
                i += 1
            elif char == '-' or char == '+':
                number = char
                i += 1
                while i < len(s) and s[i] not in signs:
                    if s[i] != " ":
                        number += s[i]
                    i += 1
                stack.append(int(number))
            elif char == '*' or char == '/':
                number = s[i+1]
                i += 2
                while i < len(s) and s[i] not in signs:
                    if s[i] != " ":
                        number += s[i]
                    i += 1
                last = stack.pop()
                if char == '*':
                    stack.append(last*int(number))
                else:
                    value = last/int(number)
                    stack.append(0 if -1 < value < 1 else int(value))

            else:
                number = ""
                while i < len(s) and s[i] not in signs:
                    if s[i] != " ":
                        number += s[i]
                    i += 1
                stack.append(int(number))
        
        return sum(stack)