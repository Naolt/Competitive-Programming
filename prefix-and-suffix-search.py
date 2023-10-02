class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words
        self.dict = defaultdict(None)
        self.size = len(words)
        
        for index in range(self.size-1,-1,-1):
            word = self.words[index]
            wordSize = len(word)
            
            for i in range(wordSize):
                for j in range(wordSize):
                    key = (word[:i+1],word[j:])
                    if key not in self.dict:
                        self.dict[key] = index
    
    def f(self, pref: str, suff: str) -> int:
        key = (pref,suff)

        if key not in self.dict:
            return -1
        return self.dict[key]