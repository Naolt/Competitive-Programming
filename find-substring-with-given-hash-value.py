class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        size = len(s)
        value = {chr(ord('a')+i):i+1 for i in range(26)}
        pows = {i:pow(power,i,modulo) for i in range(k)}
        answer = -1
        start = 0
        for i in range(k):
            start = (start + (pows[i] * value[s[size-k+i]]))% modulo
        if start == hashValue:
            answer=size - k
        
        for i in range(size-k-1,-1,-1):
            start = (start-(pows[k-1]*value[s[k+i]])) % modulo
            start *= power
            start += value[s[i]]
            
            if start%modulo == hashValue:
                answer = i
        
        return s[answer:answer+k]