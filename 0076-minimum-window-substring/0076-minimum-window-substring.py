class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = collections.Counter(t)
        letterDict = collections.defaultdict(int)
        left,right = 0,0
        size = len(s)
        l = 0
        r = size+1
        matched = 0
        while right < size+1:
            print(left,right)
            while left < size and matched == len(target):
                if r - l > right - left:
                    l = left
                    r = right
                if s[left] in letterDict:
                    letterDict[s[left]] -= 1
                    if letterDict[s[left]] < target[s[left]]:
                        matched -= 1
                left += 1

            if right == size:
                break
            if s[right] in target:
                letterDict[s[right]] += 1
                if letterDict[s[right]] == target[s[right]]:
                    matched += 1
            right += 1
        if r < size+1:
            return s[l:r]
        else:
            return ""
        
        