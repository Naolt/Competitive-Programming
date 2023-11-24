class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        childDic = defaultdict(list)
        root = None
        for emp,head in enumerate(manager):
            if head == -1:
                root = emp
            childDic[head].append(emp)

        
        def getMaxDepth(root):
            if root not in childDic:
                return 0         
            depth = 0
            for child in childDic[root]:
                depth = max(depth,getMaxDepth(child))
            
            return depth + informTime[root]

        return getMaxDepth(root)