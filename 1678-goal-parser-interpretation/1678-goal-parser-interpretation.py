"""
approach
 - create a dictionary to map the characters to their interpretation
 - 


"""


class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
       
        
        result = ""
        index = 0
        size = len(command)
        
        while(index < size):
            
            if command[index] == "(":
                if command[index+1] == ")":
                    result += "o"
                    index +=2
                else:
                    result += "al"
                    index += 4
                
            else:
                result += "G"
                index += 1
            
        return result
        