class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = collections.Counter(s1)
        window = collections.Counter(s2[0:len(s1)-1])
        windowSize,size = len(s1),len(s2)
        for i in range(windowSize-1,size):
            # print(window)
            if s2[i] not in window:
                window[s2[i]] = 1
            else:
                window[s2[i]] += 1
            if target == window:
                return True
            # print("left",s2[i-windowSize+1])
            window[s2[i-windowSize+1]] -= 1
            if window[s2[i-windowSize+1]] == 0:
                del window[s2[i-windowSize+1]]
        return False