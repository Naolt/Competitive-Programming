class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        counts = list(Counter(deck).values())
        total = counts[0]
        for num in counts:
            total = gcd(total,num)
        return total > 1