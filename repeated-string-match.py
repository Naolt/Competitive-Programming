class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        def kmp(pattern, text):
            n = len(text)
            m = len(pattern)
            pi = compute_prefix(pattern)
            j = 0
            i = 0
            ans = 0
            
            while i < n:
                
                while j > 0 and pattern[j] != text[i]:
                    if ans > 1:
                        return -1
                    j = pi[j-1]
                if pattern[j] == text[i]:
                    j += 1
                
                if j == m:
                    return ans + 1

                if i == n-1:
                    if j == 0:
                        if ans > 1:
                            return -1
                    ans += 1
                    i = -1
          
                i += 1
            return -1

        def compute_prefix(pattern):
            m = len(pattern)
            pi = [0]*m
            j = 0
            for i in range(1, m):
                while j > 0 and pattern[j] != pattern[i]:
                    j = pi[j-1]
                if pattern[j] == pattern[i]:
                    j += 1
                pi[i] = j
            return pi
        answer = kmp(b,a)
        
        return answer