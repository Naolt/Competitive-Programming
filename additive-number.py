class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        return self.backtrack(0,[],num)
    def backtrack(self,idx,arr,num):
        if len(arr) == 3:
            if (arr[0] + arr[1] == arr[2]):
                if idx >= len(num):
                    return True
                return self.backtrack(idx,[arr[1],arr[2]],num)
            return False
            
        size = len(num)
        for i in range(idx,size):
            val = num[idx:i+1]
            if len(val)>1 and val[0] == "0":
                break
            if len(arr) < 3:
                arr.append(int(val))
                if self.backtrack(i+1,arr[:],num):
                    return True
                arr.pop()
        
        return False