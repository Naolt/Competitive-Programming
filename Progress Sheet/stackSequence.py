class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        stack = []
        p = 0
        result = True
        
        for i in range(len(pushed)):
            stack.append(pushed[i])
            
            if pushed[i] == popped[p]:
                while(True):
                    if len(popped)-1  == p or len(stack) == 0:
                        break
                    
                    val= stack.pop()
                    
                    if  val != popped[p]:
                        result = False
                        stack.append(val)
                        break
                    else:
                        p+=1
                        result = True
        val = stack.pop()
        if(val == popped[p]):
            result = True
        return result
