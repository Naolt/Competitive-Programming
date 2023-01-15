'''

'(){}[]'

step 1: 


'''


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        chars = {'[':']','{':'}','(':')'}
        for x in range(len(s)):
            if( x == 0 and s[x] in chars.values()):
                return False
            if s[x] in chars.keys() :
                stack.append(s[x])
            elif s[x] in chars.values():
                if not stack:
                    return False
                popped = stack.pop()
                if not (chars[popped] == s[x]):
                    return False
        return (not bool(stack))
