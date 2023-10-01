class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = Trie()
        words.sort()
        for word in words:
            root.insert(word)
        
        return root.findLongest(root.root,"")
        


class TrieNode:
    def __init__(self,val):
        self.val = val
        self.kids = defaultdict(None)
        self.isEOW = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode("")
        self.root.isEOW = True
    
    def insert(self,word):
        node = self.root
        
        for char in word:
            if char not in node.kids:
                node.kids[char] = TrieNode(char)
            node = node.kids[char]
        node.isEOW = True
    
    def findLongest(self,parent,total):
        
        currentMax = total
        for node in parent.kids.values():

            if node.isEOW:
                result = self.findLongest(node,total+node.val)
                if len(currentMax) < len(result):
                    currentMax = result
            
        return currentMax