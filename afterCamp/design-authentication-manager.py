"""
[5], ["aaa", 1], ["aaa", 2], [6], ["bbb", 7], ["aaa", 8], ["bbb", 10], [15]
                     7 exp    1      12 exp      ignore       15 exp    

"""


class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.dic = defaultdict()
        

    def generate(self, tokenId: str, currentTime: int) -> None:
        
        self.dic[tokenId] = currentTime+self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:

        if tokenId in self.dic and self.dic[tokenId] > currentTime:
            self.dic[tokenId] = currentTime+self.timeToLive
        
    def countUnexpiredTokens(self, currentTime: int) -> int:
        count = 0
        for value in self.dic.values():
            count += int(value > currentTime)
        return count
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)