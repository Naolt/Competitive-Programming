class Solution:
    def decodeString(self, s: str) -> str:
        if s.find('[') == -1:
            # print(s)
            if s.isdigit():
                return ""
            return s
        size = len(s)
        stack = []
        num = 0
        result = ""
        end = ""
        # find left bracket

        for i in range(size):
            # print("iterating",i,s)
            if s[i] == '[':
                stack.append(i)
                # print("appended",stack)
            elif s[i] == ']':
                # print('indexes',s,stack)
                if len(stack) == 1:
                    stack.append(i)
                    num = 0
                    print("level",result,stack )
                    # finding number
                    for j in range(stack[0]-1,-1,-1):
                        if not s[j].isdigit() or j == 0:
                            if j == 0 and s[j].isdigit():
                                print("here is the index",j,stack,s)
                                num = int(s[:stack[0]])
                            else:
                                # print("failing here",j,stack)
                                num = int(s[j+1:stack[0]])
                                print("found",s,num)
                                for k in range(j,-1,-1):
                                    if s[k] == ']' or s[k] == "[" or k == 0:
                                        if k == 0:
                                            result += s[:j+1]
                                        else:
                                            result += s[k+1:j+1]
                                        break
                                    
                                for k in range(stack[1]+1,size):
                                    if s[k] != ']' and s[k] != '[' and not s[k].isdigit():
                                        end += s[k]
                                    else:
                                        break
                                # print("after string",stack[1],end)
                            break
                    # print(num)
                    for j in range(num):
                        result += self.decodeString(s[stack[0]+1:stack[1]])
                    stack.pop()
                    stack.pop()
                    
                else:
                    stack.pop() 
        # print("result:",result)
        return result+end