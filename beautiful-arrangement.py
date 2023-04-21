class Solution:
    def countArrangement(self, n: int) -> int:
        result = [0]
        self.backtrack(1,n,result)
        return result[0]
    
    def backtrack(self,current,n,result):
        print(bin(current))
        count = current.bit_count()
        if count-1 == n:
            result[0] += 1
            return
        
        for i in range(1,n+1):
            if (1<<i) & current:
                continue
            elif not (i % count) or not (count % i):
                current |= (1 << i)
                self.backtrack(current,n,result)
                current ^= (1 << i)
        return