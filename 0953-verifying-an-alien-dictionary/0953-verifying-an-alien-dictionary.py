class Solution(object):
    def isAlienSorted(self, words, order):
                
        status = "true"
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            if len(word1)>len(word2):
              
                for j in range(len(word1)):
                    if j == len(word2) and status == "true":
                        status = "false"
                        break
                    if order.index(word2[j]) < order.index(word1[j]):
                        status = "false"
                        break
                    elif order.index(word2[j]) > order.index(word1[j]):
                        break
                  
                    
            elif len(word1) < len(word2):
                for j in range(len(word1)):
                    if j == len(word1) and status == "true":
                        status = "false"
                        break
                    if order.index(word2[j]) < order.index(word1[j]):
                       
                        status = "false"
                        break
                    elif order.index(word2[j]) > order.index(word1[j]):
                        break
                  
                    
            else:
                if (word1 == word2):continue
                else:
                    for j in range(len(word1)):
                        if order.index(word2[j]) < order.index(word1[j]):
                            status = "false"
                            break
                        elif order.index(word2[j]) > order.index(word1[j]):
                            break
        if status == "true":
            return True
        else:
            return False
        
                
            