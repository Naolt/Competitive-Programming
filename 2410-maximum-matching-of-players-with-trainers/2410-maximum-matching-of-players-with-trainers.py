class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        player,trainer = 0,0
        playersSize,trainersSize = len(players),len(trainers)
        result = 0
        while player < playersSize and trainer < trainersSize:
            
            if players[player] <= trainers[trainer]:
                result += 1
                player += 1
                trainer += 1
            else:
                trainer += 1
                
        return result