class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        ["flower","flow","flight","gfl"]   
        """
        longest = ""
        strs.sort(key=len)
        if len(strs) == 1:
            return strs[0]
    
        for i in range(1,len(strs[0])+1):
	        found = True
	        for word in strs:
		    #print((strs[0])[0:i],word)
		
		        if (strs[0])[0:i] in word:
			        if word.index((strs[0])[0:i]) != 0:
				    found = False
				    break
		        else: 
			        found = False
			        break

			
	        if found: longest = (strs[0])[0:i]
       
        return longest
