class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counts = list(Counter(deck).values())
        total = counts[0]
        for num in counts:
            total = self.gcd(total,num)
        return total > 1
    def gcd(self,a,b):
        if b == 0:
            return a
        return self.gcd(b,a%b)