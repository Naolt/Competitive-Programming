class Solution:
    def simplifyPath(self,path):
        tokens = path.split('/')
        stack = []
        size = len(tokens)
        for i in range(1,size):
            if stack and tokens[i] == "..":
                stack.pop()
            elif tokens[i] != "" and tokens[i] != '.' and tokens[i] != "..":
                stack.append(tokens[i])
        
        return "/"+"/".join(stack)