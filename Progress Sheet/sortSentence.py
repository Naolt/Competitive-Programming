class Solution:
    def sortSentence(self, s: str):
        if(s.rstrip() != s.lstrip()):
            return
        if(not(s.replace(' ','').isalnum())):
            return
        if (not(2 <= len(s) and len(s) <= 200)):
            return
        if(s.find('  ') != -1):
            return
        sent = s.split(' ')
        if(len(sent)< 1 and len(sent)>9	):
            return 
		#print('1000'>'10000')
        for x in range(len(sent)-1):
            for y in range(len(sent)-1):
                if(sent[y][len(sent[y])-1]>sent[y+1][len(sent[y+1])-1]):
                    temp = sent[y]
                    sent[y] = sent[y+1]
                    sent[y+1] = temp
        newSent = ''
        for word in sent:
            newSent+=word.removesuffix(word[len(word)-1])+' '
        newSent = newSent.rstrip()
        return newSent
