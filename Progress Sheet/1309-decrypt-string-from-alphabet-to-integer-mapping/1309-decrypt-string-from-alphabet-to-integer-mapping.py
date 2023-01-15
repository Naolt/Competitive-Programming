"""

s = "1326#10#11#12"
                i
               j

str = aczjk
        
Approach:
 - create dictionary for letter mapping
 - iterate over each character and for each character iterate using second counter 2 more steps
 - if there is # sign on the 3rd step convert the the string up to the second iterator to letter and append it to      the string and increment the first iterator to the position after second iterator
 - 
 - if there is no # sign on the 3rd step convert the letter on the first iterator and append to the string
  - set j equal to i on each iteration
  -if it reaches end of string before getting # convert each letter on the first iterator and append it to the string
 



"""


class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        dictn = {1:"a"}
        
        total = ""
        for i in range(1,26):
            dictn[i+1] =  chr(ord("a")+i)
        
        i = 0
        j = 2
        
        if len(s) < 3:
            while(i != len(s)):
                total +=dictn[int(s[i])]
            return total
        
        
        while(i+2 < len(s)):
            if s[j] == "#":
                total += dictn[int(s[i:j])]
                i +=3
                j = i+2
            else:
                total += dictn[int(s[i])]
                i +=1
                j = i+2
        if i < len(s):
            while i!=len(s):
                
                total +=dictn[int(s[i])]
                i+=1
                
        return total
                
                        
                    
        
        