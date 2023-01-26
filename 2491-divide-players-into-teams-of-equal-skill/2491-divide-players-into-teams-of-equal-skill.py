class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        
        left = 0
        right = len(skill)-1
        
        result = skill[left] * skill[right]
        left += 1
        right -= 1
        if len(skill) == 2:
            return result
        
        while left < right:
            
            if skill[left] + skill[right] != skill[left-1] + skill[right+1]:
                return -1
            else:
                result += (skill[left] * skill[right])
                left += 1
                right -= 1
                
        return result
        
        