class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = Trie()

        for word in words:
            root.insert(word)
        
        answer = []
        for word in words:
            answer.append(root.search(word))
        
        return answer



class TrieNode:
    def __init__(self,val):
        self.val = val
        self.kids = defaultdict(None)
        self.count = 0
    
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
            node.count += 1
    
    def search(self,word):
        total = 0
        node = self.root

        for char in word:
            node = node.kids[char]
            total += node.count

        return total