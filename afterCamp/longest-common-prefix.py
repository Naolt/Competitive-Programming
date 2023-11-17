class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for word in strs:
            if not word:
                return ""
            trie.insert(word)
        return trie.getLongestPrefix(len(strs))



class Trie:
    def __init__(self):
        self.root = TrieNode('*')
    
    def insert(self,word):
        root = self.root

        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode(char)
            root = root.children[char]
            root.count += 1
            
    
    def getLongestPrefix(self,size):
        root = self.root
        length = ""
        while len(root.children) == 1:
            print(root.val,root.children)
            char = max(root.children)
            root = root.children[char]
            if root.count == size:
                length += char
            else:
                break
        
        return length





class TrieNode:
    def __init__(self,val):
        self.val = val
        self.count = 0
        self.children = defaultdict(TrieNode)
    
    
            

    
        