class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        outdegree = defaultdict(int)
        players = set()
        for winner,loser in matches:
            outdegree[loser] += 1
            players.add(winner)
            players.add(loser)

        result = [[],[]]

        for player in players:
            if not outdegree[player]:
                result[0].append(player)
            if outdegree[player] == 1:
                result[1].append(player) 

        result[0].sort()
        result[1].sort()

        return result