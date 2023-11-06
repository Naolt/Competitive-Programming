class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        
        def backtrack(opened,closed,total):
            if closed > opened or max(closed,opened) > n:
                return
            if opened == closed and opened == n:
                result.append(total)
            
            backtrack(opened+1,closed,total+'(')
            backtrack(opened,closed+1,total+')')

        backtrack(0,0,"")

        return result
            



        