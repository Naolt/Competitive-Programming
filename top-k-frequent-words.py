class Word:
    def __init__(self,word,freq):
        self.word = word
        self.freq = freq
    def __lt__(self, other):
        if self.freq < other.freq: return True
        elif other.freq < self.freq: return False
        else:
            if self.word > other.word: return True
            else: return False
    def getWord():
        return self.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words = Counter(words)
        wordsList = []

        for key,value in words.items():
            wordsList.append(Word(key,value))
            
        result = list(map(lambda x:x.word,heapq.nlargest(k,wordsList)))
        return result
        # def customSort(self,x,y):
        #     if x[0] > y[0]: return x
        #     elif y[0] > x[0]: return y
        #     else:
        #         if x[1] > y[1]: return x
        #         else: return y