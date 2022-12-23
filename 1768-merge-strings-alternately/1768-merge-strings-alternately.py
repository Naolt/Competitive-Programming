"""
 word1 = "apbgc", 
              i
 word2 = "pghjklm"
            j
          
          
 approach:
    - insert the letters on word2 on odd indexes until end of word 1
    - if it reaches end of word 1 append the rest of the letters on from word2 to word1
    - 



"""


class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        length1 = len(word1)
        length2 = len(word2)
        
        list1 = list(word1)
        list2 = list(word2)
        
        #insert the letters on every odd iteration
       
        position = 1
        counter2 = 0
        print(word1,word2)
        while(position < length1 or counter2 < length2):
            if counter2 == length2:
				break
            list1.insert(position,list2[counter2])
            position += 2
            counter2 += 1
        
        mergedList2 = "".join(list2)
        mergedList1 = "".join(list1)
        
        if(counter2 < length2):
            mergedList1 += mergedList2[counter2:]
            
        
        
        return mergedList1
        