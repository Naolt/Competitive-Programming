"""
matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
            i
dict= {1:1,3:-1,2:1,}

approach:
- iterate throught the array and add each player to the dictionary as +1 for win and -1 for lose
  if it already exists add 1 on it if it wins and substract 1 if it loses
  1 lost no match
  0 lost only 1 match
 -1 lost more than 1 match
"""


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        playerDict = {}
        
        for match in matches:
#            if the player lost and is in the dictionary
            if match[1] in playerDict:
               playerDict[match[1]] -= 1
            else:
                playerDict[match[1]] = 0
            if match[0] not in playerDict:
                playerDict[match[0]] = 1
                
        answer = [[],[]]
        for key,value in playerDict.items():
            if value == 1:
                answer[0].append(key)
            elif value == 0:
                answer[1].append(key)
        
        answer[0].sort()
        answer[1].sort()
        return answer
                    
        
        