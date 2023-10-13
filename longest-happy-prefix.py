class Solution:
    def longestPrefix(self, s: str) -> str:
        size = len(s)
        pi = [0]*size
        length = 0
        i = 1

        while i < size:
            if s[i] == s[length]:
                length += 1
                pi[i] = length
                i += 1
            else:
                if length != 0:
                    length = pi[length-1]
                else:
                    pi[i] = 0
                    i += 1
        # print("abcd"[2:3])
        size_index = list(map(lambda x:(x[1],x[0]),enumerate(pi)))
        # size_index.sort(reverse=True)
        # print(size_index[0])
        return s[size_index[-1][1]-(size_index[-1][0]-1):size_index[-1][1]+1]