class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        sa = len(a)
        sb = len(b)
        div = 1
        if sa == 1:
            div = sb*sa
        else:
            div = (sb//sa) + 1
        search = a*div

        index = search.find(b)

        if index > -1:
            return div
        else:
            return -1