class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        matched = {}
        used = {}

        for i in range(len(s)):
            if (s[i] in matched and matched[s[i]] != t[i]) or (t[i] in used and used[t[i]] != s[i]):
                return False
            matched[s[i]] = t[i]
            used[t[i]] = s[i]
        
        return True
            
            

        