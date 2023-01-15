class Solution(object):
    def build_hashmap(self, s):
        hashmap = {}
        for letter in s:
            if letter not in hashmap:
                hashmap[letter] = 1
            else:
                hashmap[letter] += 1
        return hashmap
    
    def findAnagrams(self, s, p):
        # Time complexity: O(n * len(P)) ~= O(n).
        # Space complexity: O(len(s) + len(p)).
        
        m, n, res = len(s), len(p), []
        
        # Build hashmap of p.
        hashmapP = self.build_hashmap(p)
        
        for beg in range(m-n+1):    
            if beg == 0:
                # Build hashmap of s.
                hashmapS = self.build_hashmap(s[:n])
            else:
                # In dynamic variant, Remove value at left side of window.
                hashmapS[s[beg-1]] -= 1
                
                # Take into account new right side of window.
                if s[beg+n-1] in hashmapS:
                    hashmapS[s[beg+n-1]] += 1
                else:
                    hashmapS[s[beg+n-1]] = 1
            
            # Compare the 2 hashmaps to know whether s and p are anagrams or not.
            tmp = 0
            for letter in hashmapP:
                # Count only letters who belong in both hashmaps.
                if letter in hashmapS and hashmapS[letter] == hashmapP[letter]:
                    tmp += hashmapS[letter] 
        
            if tmp == sum(hashmapP.values()):
                res.append(beg)

        return res