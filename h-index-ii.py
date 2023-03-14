class Solution:
    def hIndex(self, citations: List[int]) -> int:
        size = len(citations)
        left = -1
        right = size
        while left + 1 < right:
            middle = left + (right-left)//2
            print(left,middle,right)
            if citations[middle] == 0:
                left = middle
            elif size - middle > citations[middle]:
                left = middle
            else:
                right = middle

        return size-left-1