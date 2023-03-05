class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        positionSpeed = [[value,speed[index]] for index,value in enumerate(position)]
        positionSpeed.sort(reverse=True)
        result = []
        for position,speed in positionSpeed:
            distance = (target-position)/speed
            if not result or result[-1] < distance:
                result.append(distance)
        return len(result)