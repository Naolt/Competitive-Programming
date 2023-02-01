class Solution:
    def compress(self, chars: List[str]) -> int:
        right = 0
        left = 0
        count = 0
        size = len(chars)
        k = 0
        while left < size:    
            letterCount = 0
            while(right < size and chars[right] == chars[left]):
                letterCount += 1
                right += 1
            chars[k] = chars[left]
            k += 1
            left += letterCount
            count +=  1
            if letterCount > 1:
                length = len(str(letterCount)) 
                for i in range(length):
                    chars[k+i] = str(letterCount)[i] 
                k += length
                count +=  length
            
        return count