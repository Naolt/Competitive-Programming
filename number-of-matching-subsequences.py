class TrieNode:
    def __init__(self,val):
        self.val = val
        self.kids = defaultdict(None)
        self.count = 0

class Solution:

    def __init__(self):
        self.root = TrieNode("*")

    def add(self, word):
        node = self.root

        for char in word:
            if char not in node.kids:
                node.kids[char] = TrieNode(char)
            node = node.kids[char]    
        
        node.count += 1

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        for word in words:
            self.add(word)
        
        indexMap = defaultdict(list)

        for idx, ch in enumerate(s):
            indexMap[ch].append(idx)
        visited = set()
        def dfs(idx,current):
            
            ans = current.count
            
            for key,child in current.kids.items():
                                
                i = bisect.bisect_right(indexMap[key], idx)
                print(key,idx)
                if i == len(indexMap[key]):
                    continue
                ans += dfs(indexMap[key][i],child)

            return ans

        return dfs(-1,self.root)