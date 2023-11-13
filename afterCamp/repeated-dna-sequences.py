class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        mod = 10**9 + 7
        dic = {}
        hashed = 0
        myOrd = {'A':1,'C':2,'G':3,'T':4}



        for i in range(10):
            hashed *= 4
            hashed += 4*myOrd[s[i]]
        dic[hashed] = [1,0]

        for i in range(10,len(s)):
            hashed -= pow(4,10,mod)*myOrd[s[i-10]]
            hashed *= 4
            hashed += 4*myOrd[s[i]]
            if hashed not in dic:
                dic[hashed] = [1,i-9]
            else:
                dic[hashed][0] += 1
        result = []
        for key,[count,index] in dic.items():
            if count > 1:
                result.append(s[index:index+10])
        
        return result
            






        