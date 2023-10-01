class TrieNode:
    def __init__(self,letter,val):
        self.letter = letter
        self.val = val
        self.kids = defaultdict(None)
    


class MapSum:

    def __init__(self):
        self.root = TrieNode("*",0)
        self.dic = defaultdict(int)
        

    def insert(self, key: str, val: int) -> None:
        node = self.root
        exists = True if key in self.dic else False
        value = self.dic[key]
        self.dic[key] = val

        for char in key:
            if char not in node.kids:
                node.kids[char] = TrieNode(char,val)
            else:
                if exists:
                    node.kids[char].val += val-value
                else:
                    node.kids[char].val += val
            node = node.kids[char]
        
    def sum(self, prefix: str) -> int:
        total = 0
        node = self.root
        for char in prefix:
            if char not in node.kids:
                return 0
            total = node.kids[char].val
            node = node.kids[char]
        
        return total

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)