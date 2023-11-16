class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        spaces,size,left = 0,0,0
        for i in range(len(words)):
            size += len(words[i])
            if size+spaces > maxWidth:
                size -= len(words[i])
                result.append((left,i,spaces + maxWidth - (size+spaces)))
                spaces = 0
                left = i
                size = len(words[i])
            spaces += 1
        result.append((left,len(words),spaces + maxWidth - (size+spaces)))
        answer = []
        last = result.pop()
        print(result)
        for start,end,sp in result:
            txt = ""
            for i in range(start,end-1):
                spSize = (end-i)-1
                cut = 0 if spSize == 0 else ceil(sp/spSize)
                txt += words[i]
                txt += " "*min(cut,sp)
                sp -= cut
            txt += words[end-1]
            txt += " "*(sp)
            answer.append(txt)
        txt = ""
        s = last[-1]
        for i in range(last[0],last[1]-1):
            txt += words[i]
            txt += " "
            s -= 1

        txt += words[last[1]-1]
        txt += " "*s

        answer.append(txt)

        return answer
        

        

