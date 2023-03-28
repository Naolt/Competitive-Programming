class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        self.backtrack(s,0,[],result)
        return result

    def backtrack(self,s,idx,current,result):
        if idx >= len(s):
            if len(current) == 4:
                result.append('.'.join(current))
            return

        if len(current) >= 4:
            return
        size = len(s)
        for i in range(idx,size):
            num = s[idx:i+1]
            if( len(num) > 1 and num[0] == "0") or int(num) > 255:
                continue
            current.append(num)
            self.backtrack(s,i+1,current,result)
            current.pop()
        
        return