class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort(reverse = True)
        
        left = 0
        right = len(people)-1
        count = 0
        
        while left <= right:
            print(left,right,count)
            if people[left] + people[right] <= limit:
                count += 1
                left += 1
                right -= 1
            else:
                count += 1
                left += 1
                
        return count
            