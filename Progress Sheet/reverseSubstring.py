"""
(u(love)i)a

a
u
e
v
o
l
i
___
 char = )
 reversed = iloveu 


for char in string
    if char is )
        reversed = ''
        while (temp := stack.pop()) != '(':
            reversed+=temp
        if(charindex == len(string-1))"
        return reversed
        stack.append(reversed)
    else stack.append(char)
        
"""


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        open = 0
        close = 0
        result = ''
        for i in range(len(s)):

            if s[i] == ')':
                close +=1
                reversed = ''
                while (temp:= stack.pop()) != '(':
                    reversed += temp
                if open == close:
                    result += reversed
                for y in range(len(reversed)):
                    stack.append(reversed[y])
            else:
                if s[i] == '(':
                    open += 1
                if open == close and s[i] not in '()':
                    result += s[i]
                else:
                    stack.append(s[i])
        return result

