class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        dic = Counter(s1)
        window = len(s1)
        match = 0

        for i in range(len(s2)):
            if s2[i] in dic:
                dic[s2[i]] -= 1
                if dic[s2[i]] == 0:
                    match += 1
            if i >= window and s2[i-window] in dic:
                if dic[s2[i-window]] == 0:
                    match -= 1
                dic[s2[i-window]] += 1

            if match == len(dic):
                return True

        return False