class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        dict = set()
        for s,d in edges:
            if s in dict:
                return s
            if d in dict:
                return d
            dict.add(s)
            dict.add(d)