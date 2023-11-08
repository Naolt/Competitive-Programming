class Solution:
    def longestPalindrome(self, words: List[str]) -> int:

        dic = Counter(words)
        total = 0
        odd = 0
        
        for word,value in dic.items():
            if word[0] != word[1] and word[::-1] in dic:
                total += min(value,dic[word[::-1]])*2
            elif word[0] == word[1]:
                if value % 2 == 0:
                    total += value*2
                else:
                    total += (value-1)*2
                    odd += 1

        if odd > 0:
            total += 2

        return total



            

            
        

        