class Solution:
    def minTimeToType(self, word: str) -> int:
        rep = {chr(ord("a")+i):i+1 for i in range(26)}

        cur = 'a'
        total = 0
        for char in word:
            first = abs(rep[cur]-rep[char])
            second = min(rep['z']-rep[cur],rep[cur]) + min(rep['z'] - rep[char],rep[char])
            total += min(first,second)+1
            cur = char

        return total
