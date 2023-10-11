class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        heaters.sort()

        max_ = 0

        for house in houses:
            left = bisect_left(heaters,house)
            if left == len(heaters):
                left -= 1
            if left == 0:
                max_ = max(abs(heaters[left]-house),max_)
            else:
                print(left)
                max_ = max(min(abs(heaters[left]-house),abs(heaters[left-1]-house)),max_)

        return max_