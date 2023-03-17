class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        balancedSize = n//4
        dic = Counter(s)
        needed = self.getExpected(s)
        if needed == 1:
            return 1
        if len(dic) == 1:
            return needed
        overIndexes = self.getOverIndex(s,balancedSize,dic)
        minFound = float('inf')
        for left in overIndexes:
            newDict = dict(dic)
            if newDict[s[left]] > balancedSize:
                right = left
                k = needed
                while k > 0 and right < n:
                    if newDict[s[right]] > balancedSize:
                        k -= 1
                        newDict[s[right]] -= 1
                    right += 1
                if k == 0: 
                    minFound = min(minFound,right-left)
        if not overIndexes:
            return 0
        return minFound
    def getExpected(self,s):
        n = len(s)
        balancedSize = n//4
        dic = Counter(s)
        count = 0
        for key,value in dic.items():
            if value <= balancedSize:
                count += value
            elif value > balancedSize:
                count += balancedSize
        return n-count
    def getOverIndex(self,s,target,dic):
        n = len(s)
        result = []
        for i in range(n):
            if dic[s[i]] > target:
                result.append(i)
        return result